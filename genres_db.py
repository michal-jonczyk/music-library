from config import Session
from models import Genre


def get_genres():
    with Session() as session:
        genres = session.query(Genre).all()

        return genres