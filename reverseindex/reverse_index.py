from pymongo import MongoClient
import json
import csv
from bson import json_util
from collections import defaultdict
import sys
import Preprocessor


preprocessor = Preprocessor.Preprocessor()


client = MongoClient("localhost")
db = client.crawlerdb_WORK_TFIDF_3
collection = db.lower_without_punctuation_with_SW

client_TO = MongoClient("localhost")
db_TO = client_TO.crawlerdb_WORK_TFIDF_3
collection_TO = db_TO.crawlerdb_INVERSE_INDEX

#Returns cursor with all documents, can be iterated
cursor = collection.find({},{ "_id": 1, "text": 1})
ergebDict = defaultdict(list)

#Iterate through all documents
for doc in cursor:
   try:
      beforeTokenize = doc['text'].lower()
      withTokenize = preprocessor.tokenizing_complete(beforeTokenize)
      withStemming = preprocessor.stemming_words(withTokenize)
   except (KeyError, AttributeError) as e:
      pass   
   for j in withStemming:
      try:
         ergebDict[j].append(str(doc['_id']))
      except TypeError:
         pass         


#Iteriert ergebDict, speichert Zeile in tempörärer dict und speichert diesen als Dokument
#dict nimmt keine List an -> Muss als Tupel gespeichert werden
for key,value in ergebDict.items():
   t = tuple(value)
   zwischDict = {"word": key, "documents": t}
   collection_TO.insert_one(zwischDict)


#Gette neue Daten -> Überprüfen ob korrekt gespeichert
#cursor_TO = collection_TO.find().limit(10)
#for doc in cursor_TO:
#   print(doc)

#Save data locally as .csv-File
#w = csv.writer(open("output.csv", "w"))
#for key, val in ergebDict.items():
#   w.writerow([key, val])
    
    

