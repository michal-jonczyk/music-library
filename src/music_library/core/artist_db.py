from music_library.core.config import Session
from music_library.core.models import Artist,Album


def get_artists():
    with Session() as session:
        artist = session.query(Artist).all()

        return artist


def save_artist(artist):
    with Session() as session:
        session.add(artist)
        session.commit()


def update_artist(artist):
    with Session() as session:
        session.merge(artist)
        session.commit()


def artist_has_albums(artist_id):
    with Session() as session:
        count = session.query(Album).filter(Album.artist_id==artist_id).count()
        return count


def delete_artist(artist):
    with Session() as session:
        obj = session.get(Artist,artist.id)
        session.delete(obj)
        session.commit()