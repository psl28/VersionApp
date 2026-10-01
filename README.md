# VersionApp v1.3.0

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
python app_missing.py
```

Working directory:

```text
backend
```

Health URL:

```text
http://127.0.0.1:5000/api/status
```

> **Intentional test condition:** `app_missing.py` does not exist. The backend is expected to fail immediately. This version is designed to test installer failure handling.

## Frontend

Run command:

```bash
python -m http.server 8001
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
python app_missing.py
```

The backend command is intentionally invalid for this release.

### Frontend

From the `frontend` directory:

```bash
python -m http.server 8001
```

Then open:

http://127.0.0.1:8001

## Version

This is the `v1.3.0` version for the installer experiment.

### v1.3.0 change

The backend startup command in the README intentionally points to a missing Python file.

Expected installer behavior:

```text
Environment setup succeeds
        ↓
Backend startup attempted
        ↓
Backend process exits immediately
        ↓
Installer detects failure
        ↓
Backend log tail is shown / error is surfaced
        ↓
Retry + Back are available
        ↓
No orphaned processes remain
```
