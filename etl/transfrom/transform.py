import pandas as pd

class Transform:
    """
    Transforms extracted data into intended use
    """
    def __init__(self):
        self.user_keys = ["display_name", "email", "country", "account_id"]

    def user_profile(self, raw_data) -> pd.DataFrame:
        """
        Flatten and Extract important data from current user 
        and transfrom it into a dataframe.
        """
        filtered_user = {key: raw_data[key] for key in self.user_keys if key in raw_data}
        return pd.DataFrame([filtered_user])
       
    def recently_played(self, raw_data) -> pd.Dataframe:
        """
        Flatten raw recently played tracks JSON, parses timestamps, and 
        converts duration_ms into minutes per track.
        """
        records = []
        for item in raw_data.get('items'):
            track = item.get('track')
            duration = track.get('duration_ms', 0)
            album = track.get('album')
            artist = track.get('artists')
            played_at = pd.to_datetime(item.get('played_at'))

            records.append({
                'played_date': played_at.date(),               
                'played_time': played_at.strftime('%H:%M:%S'),
                'track_id': track.get('id'),
                'track_name': track.get('name'),
                'artist_id': artist[0].get('id') if artist else "N/A",
                'artist_name': artist[0].get('name') if artist else 'Unknown Artist',
                'album_name': album.get('name'),
                'duration_ms': duration,
                'duration_minutes': round(duration / (1000 * 60), 2),
            })
        return pd.DataFrame(records)

