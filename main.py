from dotenv import load_dotenv
from etl.extract.extract import Extract
from etl.transfrom.transform import Transform
from etl.load.load import Load
import json
import pandas as pd

load_dotenv()
extractor = Extract()
transformer = Transform()
loader = Load()

# Show all columns and rows without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

# Test User Func
user = extractor.get_user()
#print(type(user))
#print(json.dumps(user,indent=5))
transformed_user = transformer.user_profile(user)
print(transformed_user)
loader.insert_to_table("user_profile",transformed_user)


# Test Recently Played Tracks Funck
recent = extractor.get_user_recently_played(50)
#print(type(recent))
#print(json.dumps(recent, indent=5))
transformed_recent = transformer.recently_played(recent)
#print(transformed_recent)
loader.insert_to_table("recently_played_tracks", transformed_recent)


top_tracks = extractor.get_user_top_tracks(50)
#print(type(top_tracks))
#print(json.dumps(top_tracks, indent=5))
transformed_top_tracks = transformer.top_tracks(top_tracks)
#print(transformed_top_tracks)
loader.insert_to_table("top_tracks", transformed_top_tracks)

top_artists = extractor.get_user_top_artists(50)
#print(type(top_artists))
#print(json.dumps(top_artists, indent=5))
transformed_top_artists = transformer.top_artists(top_artists)
#print(transformed_top_artists)
loader.insert_to_table("top_artists",transformed_top_artists)