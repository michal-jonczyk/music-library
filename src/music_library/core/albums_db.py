from music_library.core.config import SessionLocal
from sqlalchemy.orm import joinedload
from music_library.core.models import Album

def get_albums():
    with SessionLocal() as session:
        albums = session.query(Album).options(joinedload(Album.artist),joinedload(Album.genre)).all()

        return albums


def save_album(album):
    with SessionLocal() as session:
        session.add(album)
        session.commit()


def delete_album(album):
    with SessionLocal() as session:
        session.delete(album)
        session.commit()


def update_album(album):
    with SessionLocal() as session:
        session.merge(album)
        session.commit()