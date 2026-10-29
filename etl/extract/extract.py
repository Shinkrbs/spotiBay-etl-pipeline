import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Extract:
    def __init__(self):
        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        scope = "user-top-read user-read-recently-played user-read-email user-read-private"

        self.client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope=scope,
            )
        )

    def get_user(self):
        """
        Get user information
        """
        try:
            print("Retrieving user information")
            user = self.client.current_user()
            return user
        except Exception as e:
            print(f"Failed fetching profile: {e}")
            raise