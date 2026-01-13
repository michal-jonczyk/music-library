from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from music_library.api.database import get_db
from music_library.core.models import Artist

app = FastAPI(title="Music Library API")


class ArtistCreate(BaseModel):
    name: str
    description: str | None = None


class ArtistOut(BaseModel):
    id: int
    name: str
    description: str | None = None  # <- ważne


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/artists", response_model=list[ArtistOut])
def get_artists(db: Session = Depends(get_db)):
    return db.query(Artist).all()


@app.post("/artists", status_code=status.HTTP_201_CREATED, response_model=ArtistOut)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    new_artist = Artist(name=artist.name, description=artist.description)
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist


@app.get("/artists/{artist_id}", response_model=ArtistOut)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist


@app.delete("/artists/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(artist)
    db.commit()
    return


@app.put("/artists/{artist_id}", response_model=ArtistOut)
def update_artist(artist_id: int, artist: ArtistCreate, db: Session = Depends(get_db)):
    existing = db.query(Artist).filter(Artist.id == artist_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    existing.name = artist.name
    existing.description = artist.description
    db.commit()
    db.refresh(existing)
    return existing


