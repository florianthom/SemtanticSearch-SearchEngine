import pymongo
import json
from bson import json_util
import Preprocessor
import pprint
import re
import logging
import gensim
from gensim.models import Word2Vec


model = Word2Vec.load("word2vec.model")

try:
        w1 = ["Raub"]
        print("Raub -> ")
        model.wv.most_similar (positive=w1,topn=6)
except Exception as exception:
        print("no word 'Raub' found in vocab..")

try:
        w1 = ["Information"]
        print("\n\nInformation -> ")
        model.wv.most_similar (positive=w1)
except Exception as exception:
        print("no word 'Information' found in vocab..")

try:
        w1 = ["was"]
        print("\n\nwas -> ")
        model.wv.most_similar (positive=w1)
except Exception as exception:
        print("no word 'was' found in vocab..")

try:
        w1 = ["das"]
        print("\n\ndas -> ")
        print(model.wv['das'])
        model.wv.most_similar (positive=w1)
except Exception as exception:
        print("no word 'das' found in vocab..")


try:
        print("\n\nmodel.wv.doesnt_match(['Raub','Information','Hund','Milch'])")
        model.wv.doesnt_match(["Raub","Information","Hund","Milch"])
except Exception as exception:
        print("kein erfolg")


print(model.vocab)
print(model.wv)
