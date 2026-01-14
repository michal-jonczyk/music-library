from music_library.core.config import SessionLocal
from music_library.core.models import Genre, Album


def get_genres():
    with SessionLocal() as session:
        genres = session.query(Genre).all()
        session.expunge_all()
        return genres


def save_genre(genre):
    with SessionLocal() as session:
        session.add(genre)
        session.commit()
        session.refresh(genre)
        session.expunge(genre)


def update_genre(genre):
    with SessionLocal() as session:
        existing = session.get(Genre, genre.id)

        if existing:
            existing.name = genre.name
            session.commit()


def genre_has_albums(genre):
    with SessionLocal() as session:
        genre_id = genre.id if hasattr(genre, 'id') else genre
        count = session.query(Album).filter(Album.genre_id == genre_id).count()
        return count > 0


def delete_genre(genre):
    with SessionLocal() as session:
        genre_id = genre.id if hasattr(genre, 'id') else genre
        obj = session.get(Genre, genre_id)

        if obj:
            session.delete(obj)
            session.commit()

