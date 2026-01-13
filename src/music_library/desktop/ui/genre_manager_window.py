import tkinter as tk
from tkinter import ttk, messagebox

from music_library.core.genres_db import get_genres, delete_genre, genre_has_albums
from music_library.desktop.ui.add_genre_window import open_add_genre_window
from music_library.desktop.ui.edit_genre_window import open_edit_genre_window


def open_genre_manager_window(parent):
    window = tk.Toplevel(parent)
    window.title('Manage Genres')
    window.geometry('520x320')

    window.grab_set()
    window.transient(parent)

    tree = ttk.Treeview(window, columns=('Name',), show='headings', selectmode='browse')
    tree.heading('Name', text='Name')
    tree.column('Name', width=480)

    tree.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    genres_dict = {}

    def refresh():
        tree.delete(*tree.get_children())
        genres_dict.clear()

        genres = get_genres()
        for g in genres:
            iid = tree.insert('', 'end', values=(g.name,))
            genres_dict[iid] = g

    def get_selected_genre():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning('Error', 'Select a genre first')
            return None
        return genres_dict[selected[0]]

    def add_genre():
        open_add_genre_window(window, lambda name: refresh())

    def edit_genre():
        genre = get_selected_genre()
        if not genre:
            return
        open_edit_genre_window(window, genre, lambda *args: refresh())

    def remove_genre():
        genre = get_selected_genre()
        if not genre:
            return

        if genre_has_albums(genre):
            messagebox.showwarning('Error', 'Cannot delete genre, because albums exist')
            return

        ok = messagebox.askyesno('Confirm', f'Delete genre "{genre.name}"?')
        if not ok:
            return

        try:
            delete_genre(genre)
        except Exception:
            messagebox.showwarning('Error', 'Could not delete genre')
            return

        refresh()

    tk.Button(window, text='Add', command=add_genre).grid(row=1, column=0, sticky='w', padx=10, pady=5)
    tk.Button(window, text='Edit', command=edit_genre).grid(row=1, column=1, sticky='w', padx=10, pady=5)
    tk.Button(window, text='Delete', command=remove_genre).grid(row=1, column=2, sticky='w', padx=10, pady=5)

    refresh()
