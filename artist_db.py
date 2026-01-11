from config import Session
from models import Artist


def get_artists():
    with Session() as session:
        artist = session.query(Artist).all()

        return artist


