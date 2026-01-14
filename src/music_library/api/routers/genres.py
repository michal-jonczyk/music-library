from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from music_library.api.database import get_db
from music_library.core.models import Genre

router = APIRouter(prefix='/genres', tags=['genres'])


class GenreCreate(BaseModel):
    name: str


class GenreOut(BaseModel):
    id: int
    name: str


@router.get('', response_model=list[GenreOut])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()


@router.post('', status_code=status.HTTP_201_CREATED, response_model=GenreOut)
def create_genre(genre: GenreCreate, db: Session = Depends(get_db)):
    new_genre = Genre(name=genre.name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre


@router.put('/{genre_id}', response_model=GenreOut)
def update_genre(genre_id: int, genre: GenreCreate, db: Session = Depends(get_db)):
    existing = db.query(Genre).filter(Genre.id == genre_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail='Genre not found')

    existing.name = genre.name
    db.commit()
    db.refresh(existing)
    return existing


@router.delete('/{genre_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    existing = db.query(Genre).filter(Genre.id == genre_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail='Genre not found')

    db.delete(existing)
    db.commit()
