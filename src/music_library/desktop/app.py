import tkinter as tk
from tkinter import ttk, messagebox

from music_library.core.albums_db import get_albums,delete_album
from music_library.desktop.ui.add_album_window import open_add_album_window
from music_library.desktop.ui.artist_manager_window import open_artist_manager_window
from music_library.desktop.ui.update_album_window import open_update_album_window
from music_library.desktop.ui.genre_manager_window import open_genre_manager_window
from music_library.core.config import init_db

def refresh_treeview(tree,albums_dict,albums_cache):
    tree.delete(*tree.get_children())
    albums_dict.clear()
    albums_cache.clear()
    albums = get_albums()
    albums_cache.extend(albums)
    for album in albums:
        item_id = tree.insert("",'end',text=album,values=(
            album.artist.name,
            album.title,
            album.genre.name,
            album.release_year))

        albums_dict[item_id] = album


def delete_single_album(tree, albums_dict,albums_cache,refresh_callback):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning('Error','Select an album first.')
        return

    selected_item = selected[0]
    album = albums_dict[selected_item]

    ok = messagebox.askyesno('Confirm', f'Delete album "{album.title}"?')
    if not ok:
        return

    try:
        delete_album(album)
    except Exception:
        messagebox.showwarning('Error','Could not delete album.')
        return
    refresh_callback()




def update_single_album(root,tree, albums_dict,albums_cache,refresh_callback):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning('Error','Select an album first.')
        return
    selected_item = selected[0]
    album = albums_dict[selected_item]


    open_update_album_window(root,album,refresh_callback)



def run_app():
    init_db()
    root = tk.Tk()
    root.title('Music Library')
    root.geometry('800x300')

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add album", command=lambda: open_add_album_window(root,refresh_and_filter))
    file_menu.add_command(label="Edit album", command=lambda: update_single_album(root,tree, albums_dict,albums_cache,refresh_and_filter))
    file_menu.add_command(label="Delete album", command=lambda: delete_single_album(tree,albums_dict,albums_cache,refresh_and_filter))
    file_menu.add_command(label="Exit",command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    genres_menu = tk.Menu(menu_bar, tearoff=0)
    genres_menu.add_command(label="Manage genres",command=lambda: open_genre_manager_window(root))
    menu_bar.add_cascade(label="Genres", menu=genres_menu)

    artists_menu = tk.Menu(menu_bar, tearoff=0)
    artists_menu.add_command(label="Manage Artist",command=lambda: open_artist_manager_window(root))
    menu_bar.add_cascade(label="Artists", menu=artists_menu)

    search_frame = tk.Frame(root)
    search_frame.pack(fill='x',padx=10,pady=(10,0))

    tk.Label(search_frame, text="Search: ").pack(side='left')

    search_var = tk.StringVar()

    search_entry = tk.Entry(search_frame, textvariable=search_var)
    search_entry.pack(side='left', fill='x',expand=True,padx=8)

    tk.Button(search_frame, text="Clear",command=lambda: search_var.set("")).pack(side='left')

    albums_dict = {}
    albums_cache = []


    def apply_filter(*args):
        q = search_var.get().lower().strip()
        tree.delete(*tree.get_children())
        albums_dict.clear()
        for album in albums_cache:
            haystack = f"{album.artist.name} {album.title} {album.genre.name} {album.release_year}".lower()
            if q in haystack:
                item_id = tree.insert('','end',values=(
                    album.artist.name,
                    album.title,
                    album.genre.name,
                    album.release_year
                ))
                albums_dict[item_id] = album

    search_var.trace_add("write",apply_filter)

    tree = ttk.Treeview(root,
                        columns=('Artist','Title','Genre','Year'),
                        show='headings',
                        selectmode='browse')
    tree.heading('Artist', text='Artist')
    tree.heading('Title', text='Title')
    tree.heading('Genre', text='Genre')
    tree.heading('Year', text='Year')


    def refresh_and_filter():
        refresh_treeview(tree,albums_dict,albums_cache)
        apply_filter()


    refresh_and_filter()

    tree.pack(expand=True, fill='both')

    tree.bind('<Double-1>', lambda e: update_single_album(root,tree, albums_dict,albums_cache,refresh_and_filter))
    tree.bind('<Delete>',lambda e: delete_single_album(tree,albums_dict,albums_cache,refresh_and_filter))
    root.config(menu=menu_bar)
    root.mainloop()


if __name__ == '__main__':
    run_app()
