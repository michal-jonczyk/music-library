from albums_db import save_album
from album_form import open_album_form_window


def open_add_album_window(parent, refresh_treeview):
    open_album_form_window(parent, refresh_treeview, on_save=save_album)
