from music_library.core.config import SessionLocal
from music_library.core.models import Artist, Album


def get_artists():
    with SessionLocal() as session:
        artists = session.query(Artist).all()
        session.expunge_all()
        return artists


def save_artist(artist):
    with SessionLocal() as session:
        session.add(artist)
        session.commit()
        session.refresh(artist)
        session.expunge(artist)


def update_artist(artist):
    with SessionLocal() as session:
        existing = session.get(Artist, artist.id)

        if existing:
            existing.name = artist.name
            if hasattr(artist, 'description'):
                existing.description = artist.description

            session.commit()


def artist_has_albums(artist_id):
    with SessionLocal() as session:
        count = session.query(Album).filter(Album.artist_id == artist_id).count()
        return count > 0


def delete_artist(artist):
    with SessionLocal() as session:
        artist_id = artist.id if hasattr(artist, 'id') else artist
        obj = session.get(Artist, artist_id)

        if obj:
            session.delete(obj)
            session.commit()