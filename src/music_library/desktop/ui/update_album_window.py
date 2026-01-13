from music_library.core.albums_db import update_album
from music_library.desktop.ui.album_form import open_album_form_window


def open_update_album_window(parent, album, refresh_treeview):
    open_album_form_window(parent, refresh_treeview, album=album, on_save=update_album)
