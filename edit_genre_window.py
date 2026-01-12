import tkinter as tk
from tkinter import messagebox

from genres_db import update_genre


def open_edit_genre_window(parent,genre,on_updated):
    window = tk.Toplevel(parent)
    window.title('Edit Genre')
    window.geometry('380x140')
    window.resizable(False, False)

    window.grab_set()
    window.transient(parent)

    tk.Label(window, text='Genre name').grid(row=0, column=0, sticky='w',padx=10, pady=10)
    name_entry = tk.Entry(window, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=10)
    name_entry.insert(0,genre.name)
    name_entry.focus()


    def save():
        new_name = name_entry.get().strip()

        if not new_name:
            messagebox.showerror('Error','Genre name is required')
            return

        genre.name = new_name

        try:
            update_genre(genre)
        except Exception:
            messagebox.showwarning('Error','Could not save changes.Name might already exist')
            return

        on_updated(genre)
        window.destroy()

    tk.Button(window, text='Save',command=save).grid(
        row=1,column=0,columnspan=2,pady=10
    )
