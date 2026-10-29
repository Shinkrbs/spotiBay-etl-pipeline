from dotenv import load_dotenv
from etl.extract.extract import Extract

load_dotenv()

extractor = Extract()

# Test User Func
#user = extractor.get_user()
#print(type(user))
#print(user)

# Test Recently Played Tracks Funck
recent = extractor.get_user_recently_played(10)
print(type(recent))

for item in recent.get('items', []):
    song_name = item['track']['name']
    print(song_name)