import pymongo
import json
from bson import json_util
import Preprocessor
import pprint

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "crawlerdb"
MONGODB_COLLECTION = "crawlerdb"

preprocessor = Preprocessor.Preprocessor()



connection = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
db = connection[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

for doc in collection.find():
    print(doc)


    

