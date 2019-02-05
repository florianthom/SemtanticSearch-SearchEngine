import pymongo
import json
from bson import json_util
import Preprocessor
import pprint
import re
import logging
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017


preprocessor = Preprocessor.Preprocessor()

connection = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
MONGODB_DB = "crawlerdb_BACKUP"
db = connection[MONGODB_DB]

MONGODB_COLLECTION = "crawlerdb_BACKUP"
collection = db[MONGODB_COLLECTION]

preprocessor = Preprocessor.Preprocessor()


i=0
g=0
listTokens = []


#collection_stemm.drop()
#collection_token.drop()
logging.info("lese kollection {0}... das wird ein wenig dauern".format(collection))
for doc in collection.find():
    g=g+1
    if "_id" in doc and "number" in doc and "text" in doc and "title" in doc:
        i=i+1
        if (i%1000==0):
            logging.info ("lese {0} eintrag".format (i))
        numberstring = str(doc["number"])
        numbertoken = re.search("[0-9]+", numberstring)
        #print(numbertoken.group())
        number=numbertoken.group()
        
        ###### REMOVING PUNCTIONAL AND STOPWORDS AND MAKE TOKENS ############
        #token_text = preprocessor.tokenizing_complete(doc["text"])
        #token_title = preprocessor.tokenizing_complete(doc["title"])
        #listTokens.append(token_text)
        #listTokens.append(token_title)

        '''
        Blanko Text bloecke ohne wirkliche struktur
        '''
        listTokens.append(doc["text"])
        listTokens.append(doc["title"])

print("Dokumente in unserem Format",i)
print("Dokumente gesamt (!evtl. nicht in unserem Format)",g)

#print(listTokens)

documents = list(listTokens)

model = gensim.models.Word2Vec (documents, size=300, window=10, min_count=1, workers=10)
model.train(documents,total_examples=len(documents),epochs=15)

model.save("word2vec.model")

#w1 = ["Raub"]
#print("Raub -> \n")
#model.wv.most_similar (positive=w1,topn=6)


#w1 = ["Information"]
#print("\nInformation -> \n")
#model.wv.most_similar (positive=w1)