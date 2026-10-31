import pandas as pd

class Transform:
    """
    Transforms extracted data into intended use
    """
    def __init__(self):
        self.user_keys = ["display_name", "email", "country", "id"]

    def user_profile(self, raw_data) -> pd.DataFrame:
        """
        Flatten and Extract important data from current user 
        and transfrom it into a dataframe.
        """
        filtered_user = {key: raw_data[key] for key in self.user_keys if key in raw_data}
        return pd.DataFrame([filtered_user])
       
    def recently_played(self, raw_data) -> pd.DataFrame:
        """
        Flatten raw recently played tracks JSON, parses timestamps, and 
        converts duration_ms into minutes per track.
        """
        records = []
        for item in raw_data.get('items', []):
            track = item.get('track')
            duration = track.get('duration_ms', 0)
            album = track.get('album')
            artist = track.get('artists')

            records.append({
                'played_at': pd.to_datetime(item.get('played_at')),
                'played_date': pd.to_datetime(item.get('played_at')).date(),               
                'played_time': pd.to_datetime(item.get('played_at')).strftime('%H:%M:%S'),
                'track_id': track.get('id'),
                'track_name': track.get('name'),
                'artist_id': artist[0].get('id') if artist else None,
                'artist_name': artist[0].get('name') if artist else 'Unknown Artist',
                'album_id': album.get('id') if album else None,
                'album_name': album.get('name') if album else "Unknown Album",
                'duration_seconds': round(duration / 1000, 2),
                'duration_minutes': round(duration / (1000 * 60), 2),
            })
        return pd.DataFrame(records)

    def top_tracks(self, raw_data) -> pd.DataFrame:
        """
        Flatten and extract data from user top_tracks and adds ranking
        """
        records = []
        for rank, track in enumerate(raw_data.get('items', []), start=1):
            album = track.get('album')
            artist = track.get('artists')

            records.append({
                'rank': rank,
                'track_id': track.get('id'),
                'track_name': track.get('name'),
                'album_id': album.get('id') if album else None,
                'album_name': album.get('name') if album else "Unknown Album",
                'track_number_on_album': track.get('track_number'),
                'artist_id': artist[0].get('id') if artist else None,
                'artist_name': artist[0].get('name') if artist else "Unknown Artist"

            })
        return pd.DataFrame(records)

    def top_artists(self, raw_data)-> pd.DataFrame:
        """
        Flatten and extract data from user top artists and adds ranking
        """
        records = []
        for rank, artists in enumerate(raw_data.get('items', []), start=1):
            records.append({
                'rank': rank,
                'artist_id': artists.get('id'),
                'artist_name': artists.get('name')
            })
        return pd.DataFrame(records)
