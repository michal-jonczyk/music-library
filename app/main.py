from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI(title = "Music Library API")

artists = []
next_artist_id = 1

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/artists")
def get_artists():
    return artists

class ArtistCreate(BaseModel):
    name: str
    description: str | None=None

@app.post("/artists")
def create_artist(artist: ArtistCreate):
    global next_artist_id

    artist_data = artist.model_dump()
    artist_data["id"] = next_artist_id
    next_artist_id += 1

    artists.append(artist_data)

    return artist_data


@app.get("/artists/{artist_id}")
def get_artist(artist_id: int):
    for artist in artists:
        if artist["id"] == artist_id:
            return artist

    raise HTTPException(status_code=404, detail="Artist not found")


@app.delete("/artists/{artist_id}")
def delete_artist(artist_id: int):
    for index, artist in enumerate(artists):
        if artist["id"] == artist_id:
            artists.pop(index)
            return{"message": "Artist deleted"}

    raise HTTPException(status_code=404, detail="Artist not found")


@app.put("/artists/{artist_id}")
def update_artist(artist_id: int, artist: ArtistCreate):
    for index, existing_artist in enumerate(artists):
        if existing_artist["id"] == artist_id:
            updated_artist = artist.model_dump()
            updated_artist["id"] = artist_id
            artists[index] = updated_artist
            return updated_artist

    raise HTTPException(status_code=404, detail="Artist not found")
