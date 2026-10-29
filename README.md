# spotiBay ETL Pipeline

**spotiBay ETL Pipeline** is an automated, Object-Oriented Data Engineering pipeline designed to extract personal Spotify listening data, transform nested JSON payloads into normalized relational models, and load them into a serverless PostgreSQL database hosted on **Neon**.

## 📁 Repository Structure

The project follows a modular, Object-Oriented Programming (OOP) design pattern to isolate data flow stages:

```
spotiBay-etl-pipeline/
├── etl/
│   ├── __init__.py
│   ├── extract/
│   │   ├── __init__.py
│   │   └── extract.py         # Handles Spotify OAuth & Web API requests
│   ├── transform/
│   │   ├── __init__.py
│   │   └── transform.py       # Data cleaning, flattening, and metric calculation
│   └── load/
│       ├── __init__.py
│       └── load.py            # Neon Postgres database operations (SQLAlchemy/psycopg2)
├── .env.example
├── .gitignore
├── main.py                    # Entry point for pipeline execution
├── requirements.txt
└── README.md
```

## ⚙️ Environment & Security Setup

### 1. Prerequisites

Ensure you have Python 3.10+ installed along with the required dependencies:

```bash
pip install spotipy pandas psycopg2-binary sqlalchemy python-dotenv
```

### 2. Environment Variables (`.env`)

Create a `.env` file in the root directory. **Never commit this file to source control.**

```env
# Spotify API Configuration
SPOTIPY_CLIENT_ID="your_spotify_client_id"
SPOTIPY_CLIENT_SECRET="your_spotify_client_secret"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:8080"

# Neon PostgreSQL Database Configuration
NEON_DATABASE_URL="postgresql://user:password@ep-cool-name-123456.us-east-2.aws.neon.tech/neondb?sslmode=require"
```

> **Note on Redirect URI:** Ensure `http://127.0.0.1:8080` is added to your application's Redirect URIs in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). Do not use `localhost` or IPv6 notation `[::1]` due to strict dashboard validation and library URL parsing limits.

## 🛠️ Extraction Module Reference (`etl.extract.Extract`)

The `Extract` class encapsulates Spotify Web API interactions using `spotipy.oauth2.SpotifyOAuth`.

### OAuth Scopes Required

* `user-top-read` — Access user's top artists and tracks.
* `user-read-recently-played` — Access recently played items.
* `user-read-email` — Identify user profile email.
* `user-read-private` — Access user subscription details and profile attributes.

