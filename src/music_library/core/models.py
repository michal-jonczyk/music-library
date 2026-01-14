from sqlalchemy import Column, Integer, String,Text,ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False, unique=True)
    description = Column(Text)

    albums = relationship('Album', back_populates='artist')

    def __str__(self):
        return self.name

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45),nullable=False, unique=True)

    albums = relationship('Album', back_populates='genre')

    def __str__(self):
        return self.name


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True, autoincrement=True)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    title = Column(String(300), nullable=False)
    cover_photo = Column(String(200))
    release_year = Column(Integer, nullable=False)

    artist = relationship('Artist', back_populates='albums')
    genre = relationship('Genre', back_populates='albums')
