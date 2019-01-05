import zerorpc
from pymongo import MongoClient
import json
from bson import json_util
import random



class GetSearchResultsRPC():

    def __init__(self):
        global collectionMongo 
        collectionMongo = MongoClient("127.0.0.1:27017").crawlerdb.crawlerdb

        
    def get_results(self, searchString):
        print(searchString)
        # data muss eine liste sein (kann geändert werden, erfordert aber eine Änderung im Backend)
        data = list(collectionMongo.find({}).limit(5))#[random.randint(0, 10)]]
        print(data)
        # der return sollte vielleicht auf maximal 20 Elemente beschränkt sein
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, default=json_util.default)


def main():
    s = zerorpc.Server(GetSearchResultsRPC())
    s.bind("tcp://*:4242")
    s.run()

if __name__ == "__main__" : main()