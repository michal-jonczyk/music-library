from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from music_library.api.database import get_db
from music_library.core.models import Album, Artist, Genre

router = APIRouter(prefix="/albums", tags=["albums"])


class AlbumCreate(BaseModel):
    artist_id: int
    genre_id: int
    title: str
    release_year: int | None = None


class AlbumOut(BaseModel):
    id: int
    artist_id: int
    genre_id: int
    title: str
    release_year: int | None = None


class AlbumOutDetailed(BaseModel):
    id: int
    title: str
    genre: str
    release_year: int | None = None
    artist: str

    model_config = {"from_attributes": True}


@router.get("", response_model=list[AlbumOutDetailed])
def get_albums(db: Session = Depends(get_db)):
    albums = db.query(Album).all()
    return [
        {
            "id": a.id,
            "title": a.title,
            "release_year": a.release_year,
            "artist": a.artist.name,
            "genre": a.genre.name,
        }
        for a in albums
    ]


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AlbumOut)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    # walidacja FK (czy artist i genre istnieją)
    artist = db.query(Artist).filter(Artist.id == album.artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    genre = db.query(Genre).filter(Genre.id == album.genre_id).first()
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    new_album = Album(
        artist_id=album.artist_id,
        genre_id=album.genre_id,
        title=album.title,
        release_year=album.release_year
    )
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album


@router.get("/{album_id}", response_model=AlbumOut)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.put("/{album_id}", response_model=AlbumOut)
def update_album(album_id: int, album: AlbumCreate, db: Session = Depends(get_db)):
    existing = db.query(Album).filter(Album.id == album_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Album not found")

    artist = db.query(Artist).filter(Artist.id == album.artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    genre = db.query(Genre).filter(Genre.id == album.genre_id).first()
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    existing.artist_id = album.artist_id
    existing.genre_id = album.genre_id
    existing.title = album.title
    existing.release_year = album.release_year
    db.commit()
    db.refresh(existing)
    return existing


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    existing = db.query(Album).filter(Album.id == album_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(existing)
    db.commit()
