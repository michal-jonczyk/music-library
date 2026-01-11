from config import Session
from models import Artist


def get_artists():
    with Session() as session:
        artist = session.query(Artist).all()

        return artist


def save_artist(artist):
    with Session() as session:
        session.add(artist)
        session.commit()