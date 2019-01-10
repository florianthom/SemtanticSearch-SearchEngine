from pymongo import MongoClient
import json
import csv
from bson import json_util
from collections import defaultdict
import sys
import Preprocessor
#Preprocessor import
preprocessor = Preprocessor.Preprocessor()
#MongoDB connection
client = MongoClient("127.0.0.1:27017")
client = MongoClient('localhost', 27017)
db = client.crawlerdb   # crawl_database_1 is the db name
collection = db.crawlerdb

#Returns cursor with all documents, can be iterated
cursor = collection.find({},{ "_id": 1, "text": 1}).limit(20000)
ergebDict = defaultdict(list)

#Iterate through all documents
for doc in cursor:
   beforeTokenize = doc['text'].lower()
   withTokenize = preprocessor.tokenizing_complete(beforeTokenize)
   withStemming = preprocessor.stemming_words(withTokenize)

   for j in withStemming:
      ergebDict[j].append(doc['_id'])
#Push data to mongoDB   
collection.insert(ergebDict)

#Save data locally as .csv-File
w = csv.writer(open("output.csv", "w"))
for key, val in ergebDict.items():
   w.writerow([key, val])
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
