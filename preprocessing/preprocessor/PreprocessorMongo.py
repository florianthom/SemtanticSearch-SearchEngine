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
var1=0
jsonobjStemming = {
    "number": "",
    "stemming_text": { "stemming_text_words": [], },
    "stemming_title": { "stemming_title_words": [], },
    }

mylistStemm = []
data={}
i=0
g=0
for doc in collection.find():
    g=g+1
    if "_id" in doc and "number" in doc and "text" in doc and "title" in doc:
        i=i+1
        numberstring = str(doc["number"])
        numbertoken = re.search("[0-9]+", numberstring)
        #print(numbertoken.group())
        number=numbertoken.group()
        token_text = preprocessor.tokenizing_complete(doc["text"])
        token_title = preprocessor.tokenizing_complete(doc["title"])
        token_text = preprocessor.stemming_words(token_text)
        token_title = preprocessor.stemming_words(token_title)

        #jsonobjStemming.append(dict(number=numbertoken.group))
        #jsonobjStemming["stemming_text"]["stemming_text_words"].append(token_text)
        #jsonobjStemming["stemming_title"]["stemming_title_words"].append(token_title)
        data["number"]=number
        data["stemming_text"] = token_text
        data["stemming_title"] = token_title
        jsonobjready = data
        mylistStemm.append(jsonobjready)
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
#print(jsonobjStemming)
print(mylistStemm[0:5])

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



'''
jsonobj = {
          "a": {
              "b": {
                      "c": var1,
                      "d": var2,
                      "e": [],
                   },

                },
            }
###ebene runter gehen und anfuegen
jsobj["a"]["b"]["e"].append({"f":var3, "g":var4, "h":var5})
jsobj["a"]["b"]["e"].append({"f":var6, "g":var7, "h":var8})
'''