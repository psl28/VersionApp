# VersionApp v1.0

A small full-stack application used to experiment with a version-aware installer.

## Structure

- `backend/` - Flask API
- `frontend/` - static HTML/CSS/JavaScript frontend

## Requirements

- Python 3.9+
- `pip`

## Run manually

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
python app.py
```

The backend runs at:

http://127.0.0.1:5000

### Frontend

From the `frontend` directory, start a simple HTTP server:

```bash
python -m http.server 8000
```

Then open:

http://127.0.0.1:8000

The frontend calls the backend API at `http://127.0.0.1:5000/api/status`.

## Version

This is the base `v1.0.0` version for the installer experiment.
