import tkinter as tk
from tkinter import messagebox

from music_library.core.artist_db import save_artist
from music_library.core.models import Artist


def open_add_artist_window(parent, on_added):
    window = tk.Toplevel(parent)
    window.title('Add Artist')
    window.geometry('400x300')

    window.grab_set()
    window.transient(parent)

    tk.Label(window, text='Artist name: ').grid(row=0, column=0,sticky='w')
    name_entry = tk.Entry(window, width=40)
    name_entry.grid(row=0, column=1,sticky='w')
    name_entry.focus()


    def save():
        name = name_entry.get().strip()

        if not name:
            messagebox.showwarning('Error', 'Artist name is required.')
            return

        try:
            save_artist(Artist(name = name))
        except Exception:
            messagebox.showwarning('Error', 'Artist already exists.')
            return

        on_added(name)

        window.destroy()

    tk.Button(window, text='Save', command=save).grid(row=1, column=0,columnspan=2,pady=10)






