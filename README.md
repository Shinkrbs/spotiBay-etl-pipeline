# spotiBay ETL Pipeline

**spotiBay ETL Pipeline** is an automated, object-oriented data engineering pipeline that extracts personal Spotify listening data, transforms nested JSON into normalized records, and loads it into a PostgreSQL database hosted on **Supabase**.

## Repository Structure

```text
spotiBay-etl-pipeline/
├── etl/
│   ├── extract/
│   │   ├── __init__.py
│   │   └── extract.py         # Spotify OAuth and Web API requests
│   ├── transfrom/
│   │   ├── __init__.py
│   │   └── transform.py       # Data cleaning and flattening
│   └── load/
│       ├── __init__.py
│       └── load.py            # Supabase database operations
├── .env.example
├── .gitignore
├── main.py                    # Pipeline entry point
└── README.md
```

## Environment and Security Setup

### Prerequisites

Use Python 3.10 or newer and install the required dependencies:

```bash
pip install spotipy pandas supabase python-dotenv
```

### Environment Variables

Create a `.env` file in the repository root. Never commit this file to source control.

```env
# Spotify API Configuration
SPOTIPY_CLIENT_ID="your_spotify_client_id"
SPOTIPY_CLIENT_SECRET="your_spotify_client_secret"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:8080"

# Supabase Configuration
SUPABASE_URL="https://your-project-id.supabase.co"
SUPABASE_SERVICE_KEY="your-supabase-service-role-key"
```

The `SUPABASE_SERVICE_KEY` is a server-side secret with elevated permissions. Keep it in `.env`, ensure `.env` is ignored by Git, and never expose it in client-side code.

Ensure `http://127.0.0.1:8080` is registered as an allowed Redirect URI in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

## Running the Pipeline

After configuring Spotify and Supabase credentials, run the entry point from the repository root:

```bash
python main.py
```

The loader uses Supabase `upsert` operations to write transformed records to the target tables, including `user_profile`.

## Extraction Module Reference

The `Extract` class uses `spotipy.oauth2.SpotifyOAuth` to access the Spotify Web API.

### Required OAuth Scopes

* `user-top-read` - Access the user's top artists and tracks.
* `user-read-recently-played` - Access recently played items.
* `user-read-email` - Access the user's email.
* `user-read-private` - Access private profile information.
