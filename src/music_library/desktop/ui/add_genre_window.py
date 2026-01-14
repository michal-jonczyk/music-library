import tkinter as tk
from tkinter import messagebox

from music_library.core.genres_db import save_genre
from music_library.core.models import Genre


def open_add_genre_window(parent,on_added):
    window = tk.Toplevel(parent)
    window.title('Add Genre')
    window.geometry('400x300')
    window.resizable(False, False)

    window.grab_set()
    window.transient(parent)

    tk.Label(window, text='Genre name: ').grid(row=0, column=0, sticky='w',padx=10, pady=10)
    name_entry = tk.Entry(window, width=40)
    name_entry.grid(row=0, column=1, sticky='w',padx=10, pady=10)
    name_entry.focus()


    def save():
        name = name_entry.get().strip()

        if not name:
            messagebox.showwarning('Error','Genre name is required')
            return

        try:
            save_genre(Genre(name=name))
        except Exception:
            messagebox.showwarning('Error','Genre already exists')
            return

        on_added(name)
        window.destroy()

    tk.Button(window, text='Save', command=save).grid(row=1, column=0, columnspan=2, pady=10)
