import tkinter as tk
from tkinter import ttk

from albums_db import get_albums,delete_album
from add_album_window import open_add_album_window
from update_album_window import open_update_album_window

def refresh_treeview(tree,albums_dict):
    tree.delete(*tree.get_children())
    albums_dict.clear()

    albums = get_albums()

    for album in albums:
        item_id = tree.insert('', 'end', values=(album.artist.name, album.title, album.genre.name, album.release_year))
        albums_dict[item_id] = album


def delete_single_album(tree, albums_dict):
    selected = tree.selection()
    if not selected:
        return
    selected_item = selected[0]
    album = albums_dict[selected_item]

    delete_album(album)
    refresh_treeview(tree,albums_dict)


def update_single_album(root,tree, albums_dict):
    selected = tree.selection()
    if not selected:
        return
    selected_item = selected[0]
    album = albums_dict[selected_item]

    open_update_album_window(root,album,lambda: refresh_treeview(tree,albums_dict))



def run_app():
    root = tk.Tk()
    root.title('Music Library')
    root.geometry('800x300')

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Dodaj album", command=lambda: open_add_album_window(root, lambda: refresh_treeview(tree,albums_dict)))
    file_menu.add_command(label="Edytuj album", command=lambda: update_single_album(root,tree, albums_dict))
    file_menu.add_command(label="Usuń album", command=lambda: delete_single_album(tree,albums_dict))
    file_menu.add_command(label="Wyjdź",command=root.quit)

    menu_bar.add_cascade(label="Plik", menu=file_menu)

    tree = ttk.Treeview(root,
                        columns=('Artist','Title','Genre','Year'),
                        show='headings',
                        selectmode='browse')
    tree.heading('Artist', text='Artist')
    tree.heading('Title', text='Title')
    tree.heading('Genre', text='Genre')
    tree.heading('Year', text='Year')

    albums_dict = {}

    refresh_treeview(tree,albums_dict)

    tree.pack(expand=True, fill='both')
    root.config(menu=menu_bar)
    root.mainloop()


if __name__ == '__main__':
    run_app()