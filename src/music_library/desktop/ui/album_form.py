import tkinter as tk
from tkinter import ttk

from music_library.core.artist_db import get_artists
from music_library.core.genres_db import get_genres
from music_library.core.models import Album
from music_library.desktop.ui.add_artist_window import open_add_artist_window


def open_album_form_window(parent, refresh_treeview, album=None, on_save=None):
    window = tk.Toplevel(parent)
    window.geometry('400x300')
    window.grab_set()
    window.transient(parent)

    window.title('Edit album' if album else 'Add new album')

    tk.Label(window, text='Artist: ').grid(row=0, column=0, sticky='w')
    tk.Label(window, text='Album title: ').grid(row=1, column=0, sticky='w')
    tk.Label(window, text='Genre: ').grid(row=2, column=0, sticky='w')
    tk.Label(window, text='Release year: ').grid(row=3, column=0, sticky='w')

    artists_dict = {a.name: a for a in get_artists()}
    genres_dict = {g.name: g for g in get_genres()}

    artist_cb = ttk.Combobox(window, values=list(artists_dict.keys()), state='readonly')
    title_entry = tk.Entry(window)
    genre_cb = ttk.Combobox(window, values=list(genres_dict.keys()), state='readonly')
    year_entry = tk.Entry(window)

    def reload_artists(select_name=None):
        new_artists = {a.name: a for a in get_artists()}
        artists_dict.clear()
        artists_dict.update(new_artists)
        artist_cb['values'] = list(artists_dict.keys())
        if select_name:
            artist_cb.set(select_name)

    if album:
        artist_cb.set(album.artist.name)
        title_entry.insert(0, album.title)
        genre_cb.set(album.genre.name)
        year_entry.insert(0, album.release_year)

    artist_cb.grid(row=0, column=1, sticky='w')

    add_artist_btn = tk.Button(
        window,
        text='+',
        width=3,
        command=lambda: open_add_artist_window(window, lambda name: reload_artists(name)),
    )
    add_artist_btn.grid(row=0, column=2, sticky='w', padx=5)

    title_entry.grid(row=1, column=1, sticky='w')
    genre_cb.grid(row=2, column=1, sticky='w')
    year_entry.grid(row=3, column=1, sticky='w')

    def save():
        artist = artists_dict.get(artist_cb.get())
        title = title_entry.get().strip()
        genre = genres_dict.get(genre_cb.get())
        year_str = year_entry.get().strip()

        if not year_str.isdigit():
            tk.messagebox.showwarning('Error', 'Release year must be a number.')
            return

        release_year = int(year_str)

        if album:
            album.artist = artist
            album.title = title
            album.genre = genre
            album.release_year = release_year
            on_save(album)
        else:
            new_album = Album(
                artist=artist,
                title=title,
                genre=genre,
                release_year=release_year,
            )
            on_save(new_album)

        refresh_treeview()
        window.destroy()

    tk.Button(window, text='Save', command=save).grid(row=4, column=0, columnspan=2)
