from pymongo import MongoClient
import json
from bson import json_util
import Preprocessor

#client = MongoClient("127.0.0.1:27017")
client = MongoClient('localhost', 27017)
db = client.crawlerdb   # crawl_database_1 is the db name
collection = db.crawlerdb

collection.find({})[0]

