from dotenv import load_dotenv
from etl.extract.extract import Extract

load_dotenv()

extratcor = Extract()
user = extratcor.get_user()
print(user)