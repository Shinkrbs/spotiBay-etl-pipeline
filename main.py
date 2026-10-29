from dotenv import load_dotenv
from etl.extract.extract import Extract
import json
load_dotenv()

extractor = Extract()

# Test User Func
#user = extractor.get_user()
#print(type(user))
#print(user)

# Test Recently Played Tracks Funck
# recent = extractor.get_user_recently_played(10)
#print(type(recent))


top_tracks = extractor.get_user_top_tracks(1)
print(type(top_tracks))
print(json.dumps(top_tracks, indent=5))