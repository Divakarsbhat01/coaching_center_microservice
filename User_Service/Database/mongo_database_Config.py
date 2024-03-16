import pymongo
from Configuration.config import settings

MONGO_connection_url = settings.MONGO_connection_url
conn = pymongo.MongoClient()
db = conn.users #database
user_login_var = db.user_login #Here spam is my collection
user_id_counter_var=db.user_id_counter