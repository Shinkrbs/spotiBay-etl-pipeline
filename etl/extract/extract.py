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

    def get_user_recently_played(self, limit: int=50):
        """
        Get user recently played tracks

        Args:
        limit = optional parameter with maximum value of int 50, maximum number of items to retrieve
        """
        try:
            print("Retrieving Recently Played Tracks.")
            recently_played = self.client.current_user_recently_played(limit=limit)
            return recently_played
        except Exception as e:
            print(f"Failed to retrieve recently played tracks: {e}")
            raise

    def get_user_top_tracks(self, limit: int=50, range: str="short_term"):
        """
        Get user top tracks
        
        Args:
        limit = optional parameter with maximum value of int 50, maximum number of items to retrieve
        range = optional parameter with values "short_term", "medium_term", or "long_term"
        """
        try:
            print("Retrieving User Top Tracks")
            return self.client.current_user_top_tracks(limit=limit, time_range=range)
        except Exception as e:
            print(f"Failed to retrieve top tracks: {e}")
            raise

    def get_user_top_artists(self, limit: int=50, range: str="short_term"):
        """
        Get user top artists

        Args:
        limit = optional parameter with maximum value of int 50, maximum number of items to retrieve
        range = optional parameter with values "short_term", "medium_term", or "long_term"
        """
        try:
            print("Retrieving User Top Artists")
            return self.client.current_user_top_artists(limit=limit, time_range=range)
        except Exception as e:
            print(f"Failed to retrieve top artists: {e}")
            raise