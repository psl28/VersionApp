# VersionApp v1.4.0

A small full-stack application used to experiment with a version-aware installer.

## Structure

- `backend/` - Flask API
- `frontend/` - static HTML/CSS/JavaScript frontend

## Requirements

- Python 3.9+
- `pip`

## Backend

Run command:

```bash
python app.py
```

Working directory:

```text
backend
```

Health URL:

```text
http://127.0.0.1:5000/api/status
```

## Frontend

Run command:

```bash
python frontend_missing.py
```

Working directory:

```text
frontend
```

Ready URL:

```text
http://127.0.0.1:8001
```

## Manual Run

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
python app.py
```

The backend runs at:

http://127.0.0.1:5000

### Frontend

From the `frontend` directory, start the frontend server:

```bash
python frontend_missing.py
```

Then open:

http://127.0.0.1:8001

The frontend calls the backend API at:

http://127.0.0.1:5000/api/status

## Version

This is the `v1.4.0` version for the installer experiment.

### v1.2.0 change

The frontend startup command is intentionally invalid for this release.

The README points the installer to `frontend_missing.py`, which does not exist. This version is designed to test frontend startup failure handling.
