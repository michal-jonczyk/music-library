text
# Music Library

Desktop application and REST API for managing a personal music library.

The project consists of:
- a Tkinter desktop app for managing artists, albums and genres,
- a FastAPI backend exposing the same data via a JSON REST API (SQLAlchemy + SQLite).

---

## Features

- Add, edit and delete artists
- Add, edit and delete albums
- Manage music genres
- Assign albums to artists and genres
- Live search for albums (filter while typing)
- Double-click an album row to edit it
- Delete key shortcut to remove the selected album

---

## Tech stack

- Python
- Tkinter
- FastAPI
- SQLAlchemy (ORM)
- SQLite

---

## Project structure (simplified)

- `src/music_library/core/` – database config and SQLAlchemy models  
- `src/music_library/desktop/` – Tkinter GUI (`app.py` and windows)  
- `src/music_library/api/` – FastAPI application (`main.py`, routers)  
- `library.db` – SQLite database file (auto-created in project root)

---

## How to run the desktop app

1. Clone the repository:

   ```bash
   git clone https://github.com/michal-jonczyk/music-library.git
   cd music-library
	

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv

3.Activate the virtual environment:

   ```bash
   Windows:
   venv\Scripts\activate
   Linux/macOS:
   source venv/bin/activate

4.Install dependencies:

   ```bash
   pip install -r requirements.txt

5.Run the Tkinter application:

   ```bash
   python src/music_library/desktop/app.py