import tkinter as tk
from tkinter import ttk
from artist_db import get_artists
from genres_db import get_genres
from models import Album


def open_album_form_window(parent, refresh_treeview, album=None, on_save=None):
    window = tk.Toplevel(parent)
    window.geometry('400x300')
    window.grab_set()
    window.transient(parent)

    window.title('Edytuj album' if album else 'Dodaj nowy album')

    tk.Label(window, text='Artysta: ').grid(row=0, column=0, sticky='w')
    tk.Label(window, text='Tytuł albumu: ').grid(row=1, column=0, sticky='w')
    tk.Label(window, text='Gatunek: ').grid(row=2, column=0, sticky='w')
    tk.Label(window, text='Rok wydania: ').grid(row=3, column=0, sticky='w')

    artists_dict = {a.name: a for a in get_artists()}
    genres_dict = {g.name: g for g in get_genres()}

    artist_cb = ttk.Combobox(window, values=list(artists_dict.keys()), state='readonly')
    title_entry = tk.Entry(window)
    genre_cb = ttk.Combobox(window, values=list(genres_dict.keys()), state='readonly')
    year_entry = tk.Entry(window)

    if album:
        artist_cb.set(album.artist.name)
        title_entry.insert(0, album.title)
        genre_cb.set(album.genre.name)
        year_entry.insert(0, album.release_year)

    artist_cb.grid(row=0, column=1, sticky='w')
    title_entry.grid(row=1, column=1, sticky='w')
    genre_cb.grid(row=2, column=1, sticky='w')
    year_entry.grid(row=3, column=1, sticky='w')

    def save():
        if album:
            album.artist = artists_dict.get(artist_cb.get())
            album.title = title_entry.get()
            album.genre = genres_dict.get(genre_cb.get())
            album.release_year = year_entry.get()
            on_save(album)
        else:
            new_album = Album(
                artist=artists_dict.get(artist_cb.get()),
                title=title_entry.get(),
                genre=genres_dict.get(genre_cb.get()),
                release_year=year_entry.get()
            )
            on_save(new_album)

        refresh_treeview()
        window.destroy()

    tk.Button(window, text='Zapisz', command=save).grid(row=4, column=0, columnspan=2)
