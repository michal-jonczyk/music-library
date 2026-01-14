from fastapi import FastAPI
from music_library.api.routers.artists import router as artists_router
from music_library.api.routers.genres import router as genres_router
from music_library.api.routers.album import router as albums_router

app = FastAPI(title='Music Library API')

@app.get('/health')
def health_check():
    return {'status': 'ok'}
app.include_router(artists_router)
app.include_router(genres_router)
app.include_router(albums_router)