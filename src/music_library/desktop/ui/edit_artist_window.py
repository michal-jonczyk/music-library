import tkinter as tk
from tkinter import messagebox

from music_library.core.artist_db import update_artist

def open_edit_artist_window(parent, artist, on_updated):
    window = tk.Toplevel(parent)
    window.title('Edit Artist')
    window.geometry('420x180')

    window.grab_set()
    window.transient(parent)

    tk.Label(window,text='Artist name: ').grid(row=0,column=0,sticky='w')
    name_entry = tk.Entry(window,width=35)
    name_entry.grid(row=0,column=1,sticky='w')
    name_entry.insert(0,artist.name)
    name_entry.focus()


    def save():
        new_name = name_entry.get().strip()

        if not new_name:
            messagebox.showwarning('Error','Artist name is required.')
            return

        artist.name = new_name

        try:
            update_artist(artist)
        except:
            messagebox.showwarning('Error','Could not save changes. Name might already exist.')
            return

        on_updated()
        window.destroy()

    tk.Button(window,text='Save',command=save).grid(row=1,column=0,columnspan=2,pady=10)
