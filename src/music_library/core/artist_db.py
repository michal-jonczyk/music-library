from music_library.core.config import SessionLocal
from music_library.core.models import Artist,Album


def get_artists():
    with SessionLocal() as session:
        artist = session.query(Artist).all()

        return artist


def save_artist(artist):
    with SessionLocal() as session:
        session.add(artist)
        session.commit()


def update_artist(artist):
    with SessionLocal() as session:
        session.merge(artist)
        session.commit()


def artist_has_albums(artist_id):
    with SessionLocal() as session:
        count = session.query(Album).filter(Album.artist_id==artist_id).count()
        return count


def delete_artist(artist):
    with SessionLocal() as session:
        obj = session.get(Artist,artist.id)
        session.delete(obj)
        session.commit()