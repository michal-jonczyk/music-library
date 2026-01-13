import tkinter as tk
from tkinter import ttk, messagebox

from music_library.core.artist_db import get_artists, delete_artist, artist_has_albums
from music_library.desktop.ui.add_artist_window import open_add_artist_window
from music_library.desktop.ui.edit_artist_window import open_edit_artist_window


def open_artist_manager_window(parent):
    window = tk.Toplevel(parent)
    window.title('Manage Artists')
    window.geometry('520x320')

    window.grab_set()
    window.transient(parent)

    tree = ttk.Treeview(window,columns=('Name',),show='headings',selectmode='browse')
    tree.heading('Name',text='Name')
    tree.column('Name',width=480)

    tree.grid(row=0,column=0,columnspan=3,sticky='nsew',padx=10,pady=10)

    window.grid_rowconfigure(0,weight=1)
    window.grid_columnconfigure(0,weight=1)

    artists_dict = {}

    def refresh():
        tree.delete(*tree.get_children())
        artists_dict.clear()

        artists = get_artists()
        for a in artists:
            iid = tree.insert('','end',values=(a.name,))
            artists_dict[iid] = a


    def get_selected_artist():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning('Error','Select an artist first')
            return None
        return artists_dict[selected[0]]


    def add_artist():
        open_add_artist_window(window, lambda name: refresh())


    def edit_artist():
        artist = get_selected_artist()
        if not artist:
            return
        open_edit_artist_window(window, artist,refresh)


    def remove_artist():
        artist = get_selected_artist()
        if not artist:
            return

        if artist_has_albums(artist.id):
            messagebox.showwarning('Error','Cannot delete artist because albums exist')
            return

        ok = messagebox.askyesno('Confirm',f'Delete artist "{artist.name}"?')
        if not ok:
            return

        try:
            delete_artist(artist)
        except Exception as e:
            messagebox.showerror('Error','Could not delete artist')
            return


        refresh()

    tk.Button(window, text='Add',command=add_artist).grid(row=1,column=0,sticky='w',padx=10,pady=5)
    tk.Button(window, text='Edit',command=edit_artist).grid(row=1,column=1,sticky='w',padx=10,pady=5)
    tk.Button(window, text='Delete',command=remove_artist).grid(row=1,column=2,sticky='w',padx=10,pady=5)

    refresh()

