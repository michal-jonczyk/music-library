from music_library.core.config import SessionLocal
from music_library.core.models import Genre, Album


def get_genres():
    with SessionLocal() as session:
        genres = session.query(Genre).all()

        return genres


def save_genre(genre):
    with SessionLocal() as session:
        session.add(genre)
        session.commit()


def update_genre(genre):
    with SessionLocal() as session:
        session.merge(genre)
        session.commit()


def genre_has_albums(genre):
    with SessionLocal() as session:
        count = session.query(Album).filter(Album.genre_id == genre.id).count()
        return count > 0


def delete_genre(genre):
    with SessionLocal() as session:
        obj = session.get(Genre, genre.id)
        session.delete(obj)
        session.commit()


