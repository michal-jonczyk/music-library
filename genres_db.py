from config import Session
from models import Genre, Album


def get_genres():
    with Session() as session:
        genres = session.query(Genre).all()

        return genres


def save_genre(genre):
    with Session() as session:
        session.add(genre)
        session.commit()


def update_genre(genre):
    with Session() as session:
        session.merge(genre)
        session.commit()


def genre_has_albums(genre):
    with Session() as session:
        count = session.query(Album).filter(Album.genre_id == genre.id).count()
        return count > 0


def delete_genre(genre):
    with Session() as session:
        obj = session.get(Genre, genre.id)
        session.delete(obj)
        session.commit()


