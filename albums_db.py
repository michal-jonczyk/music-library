from config import Session
from sqlalchemy.orm import joinedload
from models import Album

def get_albums():
    with Session() as session:
        albums = session.query(Album).options(joinedload(Album.artist),joinedload(Album.genre)).all()

        return albums


def save_album(album):
    with Session() as session:
        session.add(album)
        session.commit()


def delete_album(album):
    with Session() as session:
        session.delete(album)
        session.commit()


def update_album(album):
    with Session() as session:
        session.merge(album)
        session.commit()