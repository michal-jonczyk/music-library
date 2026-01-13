from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from music_library.core.models import Base

DATABASE_URL = 'sqlite:///library.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'library.db')}"

def init_db():
    Base.metadata.create_all(bind=engine)