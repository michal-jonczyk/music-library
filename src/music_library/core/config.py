import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from music_library.core.models import Base

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
)

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'library.db')}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(bind=engine)
