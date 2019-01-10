import pymongo
import json
from bson import json_util
import Preprocessor
import pprint
import re

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "crawlerdb_BACKUP"
MONGODB_COLLECTION = "crawlerdb_BACKUP"
MONGODB_COLLECTION_TOKENIZING = "crawlerdb_tokenization"

preprocessor = Preprocessor.Preprocessor()



connection = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
db = connection[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

preprocessor = Preprocessor.Preprocessor()

########## ROHDATEN ##########
''' 
{
    'number': '1288202', 
    'location': 'Cottbus', 
    'text': 'Nach einem Fehler beim Überholen....', 
    'date': '14.12.2018', 
    '_id': ObjectId('5c2fc96788df4228e7861c93'), 
    'title': 'Fehler beim Überholen'
}
'''
########## LOWER, STOPWORDS AND PUNCTIONAL REMOVING + TOKEN AND STEMMING ##########
''' 
{
    'number': '1288202', 
    'stemming_text': ['','' .... ], 
    'stemming_title': ['','' .... ], 
    '_id': ObjectId('5c2fc96788df4228e7861c93'), 
}
'''

########## LOWER, STOPWORDS AND PUNCTIONAL REMOVING + TOKEN AND LEMMATIZATION ##########
'''
{
    'number': '1288202', 
    'lemmatization_title': [{'',''},{'',''}], 
    'lemmatization_text': [{'',''},{'',''}],
    '_id': ObjectId('5c2fc96788df4228e7861c93'),
}
'''

########## LOWER, STOPWORDS AND PUNCTIONAL REMOVING + TOKEN AND LEMMATIZATION ##########
'''
{
    'number': '1288202', 
    'lemmatization_title': [{'',''},{'',''}], 
    'lemmatization_text': [{'',''},{'',''}],
    '_id': ObjectId('5c2fc96788df4228e7861c93'),
}
'''


i=0
g=0
for doc in collection.find():
    g=g+1
    if "_id" in doc and "number" in doc and "text" in doc and "title" in doc:
        i=i+1
        numberstring = str(doc["number"])
        numbertoken = re.search("[0-9]+", numberstring)
        print(numbertoken.group())
        
    #print(i)
    #print(doc)
    x = doc
    #print(x)
    #print(x['number'])
    #print(x['title'])
    #print(x['text'])
    
    #token_title = preprocessor.tokenizing_complete(x['title'])
    #token_text = preprocessor.tokenizing_complete(x['text'])
    #token_number = re.search("[0-9]+", str(x['number']))
    #token_number = x['number']
    #thisdict =	dict(number=token_number, title=token_title, text=token_text)
    #print(thisdict)
print("records = " + str(g))
print("records with id and number = " + str(i))

'''
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
'''