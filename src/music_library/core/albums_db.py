from music_library.core.config import SessionLocal
from sqlalchemy.orm import joinedload
from music_library.core.models import Album


def get_albums():
    with SessionLocal() as session:
        albums = session.query(Album).options(
            joinedload(Album.artist),
            joinedload(Album.genre)
        ).all()

        session.expunge_all()
        return albums


def save_album(album):
    with SessionLocal() as session:
        session.add(album)
        session.commit()
        session.refresh(album)
        session.expunge(album)


def delete_album(album):
    with SessionLocal() as session:
        album_id = album.id if hasattr(album, 'id') else album
        album_to_delete = session.get(Album, album_id)

        if album_to_delete:
            session.delete(album_to_delete)
            session.commit()


def update_album(album):
    with SessionLocal() as session:
        existing = session.get(Album, album.id)

        if existing:
            existing.artist_id = album.artist.id if album.artist else None
            existing.genre_id = album.genre.id if album.genre else None
            existing.title = album.title
            existing.release_year = album.release_year

            session.commit()
            session.refresh(existing)

            album.artist_id = existing.artist_id
            album.genre_id = existing.genre_id