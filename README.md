# Music Library

Desktop application and REST API for managing a personal music library.

The project consists of:
- A **Tkinter desktop app** for managing artists, albums and genres
- A **FastAPI backend** exposing the same data via a JSON REST API
- **SQLAlchemy ORM** with SQLite database

---

## Features

### Desktop App
- Add, edit and delete artists
- Add, edit and delete albums
- Manage music genres
- Assign albums to artists and genres
- Live search for albums (filter while typing)
- Double-click an album row to edit it
- Delete key shortcut to remove the selected album

### REST API
- Full CRUD operations for Artists, Albums, and Genres
- Interactive API documentation (Swagger UI)
- JSON responses
- Input validation with Pydantic

---

## Tech Stack

- **Python 3.10+**
- **Tkinter** - GUI framework
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation
- **SQLite** - Lightweight database
- **Pytest** - Testing framework

---

## Project Structure

```
music-library/
├── src/
│   └── music_library/
│       ├── core/              # Database models and business logic
│       │   ├── models.py      # SQLAlchemy models
│       │   ├── config.py      # Database configuration
│       │   ├── albums_db.py   # Album operations
│       │   ├── artist_db.py   # Artist operations
│       │   └── genres_db.py   # Genre operations
│       ├── api/               # FastAPI application
│       │   ├── main.py        # API entry point
│       │   ├── database.py    # Database dependency
│       │   └── routers/       # API endpoints
│       │       ├── artists.py
│       │       ├── genres.py
│       │       └── album.py
│       └── desktop/           # Tkinter GUI
│           ├── app.py         # Desktop app entry point
│           └── ui/            # UI windows/dialogs
├── requirements.txt           # Python dependencies
├── library.db                 # SQLite database (auto-created)
└── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/michal-jonczyk/music-library.git
cd music-library
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Option 1: Desktop App

```bash
python src/music_library/desktop/app.py
```

The Tkinter GUI will open. You can manage your music library through the interface.

### Option 2: REST API

```bash
uvicorn music_library.api.main:app --reload
```

The API will be available at:
- **Base URL:** http://localhost:8000
- **Interactive docs (Swagger):** http://localhost:8000/docs
- **Alternative docs (ReDoc):** http://localhost:8000/redoc

---

## API Endpoints

### Health Check
- `GET /health` - Check if API is running

### Artists
- `GET /artists` - Get all artists
- `POST /artists` - Create new artist
- `GET /artists/{id}` - Get artist by ID
- `PUT /artists/{id}` - Update artist
- `DELETE /artists/{id}` - Delete artist

### Genres
- `GET /genres` - Get all genres
- `POST /genres` - Create new genre
- `PUT /genres/{id}` - Update genre
- `DELETE /genres/{id}` - Delete genre

### Albums
- `GET /albums` - Get all albums (with artist and genre details)
- `POST /albums` - Create new album
- `GET /albums/{id}` - Get album by ID
- `PUT /albums/{id}` - Update album
- `DELETE /albums/{id}` - Delete album

### Example API Usage

**Create an artist:**
```bash
curl -X POST "http://localhost:8000/artists" \
  -H "Content-Type: application/json" \
  -d '{"name": "Pink Floyd", "description": "British rock band"}'
```

**Get all albums:**
```bash
curl http://localhost:8000/albums
```

---

## Running Tests

```bash
pytest
```

To see coverage report:
```bash
pytest --cov=music_library
```

---

## Database

The application uses SQLite database which is automatically created on first run as `library.db` in the project root directory.

### Database Schema

**Artist**
- `id` (Primary Key)
- `name` (Unique, Not Null)
- `description` (Text)

**Genre**
- `id` (Primary Key)
- `name` (Unique, Not Null)

**Album**
- `id` (Primary Key)
- `artist_id` (Foreign Key → Artist)
- `genre_id` (Foreign Key → Genre)
- `title` (Not Null)
- `release_year` (Integer, Not Null)
- `cover_photo` (String)

---

## Development

### Code Quality

The project follows Python best practices:
- Type hints where applicable
- Docstrings for functions
- Separation of concerns (MVC-like architecture)
- Proper error handling

### Future Improvements

- [ ] Add authentication/authorization to API
- [ ] Add pagination to API endpoints
- [ ] Implement album cover photo upload
- [ ] Add data export/import functionality
- [ ] Deploy with Docker
- [ ] Add more comprehensive tests

---

## License

MIT License

---

## Author

Michał Jończyk
- GitHub: [@michal-jonczyk](https://github.com/michal-jonczyk)

---

## Contributing

Contributions, issues, and feature requests are welcome!
