import zerorpc
from pymongo import MongoClient
import json
from bson import json_util
import random
from SearchModule import Search




class GetSearchResultsRPC():

    def __init__(self):
        global collectionMongo 
        databaseMongo = MongoClient("127.0.0.1:27017").crawlerdb_WORK_TFIDF_3
        global search
        search = Search(databaseMongo)
        
    def get_results(self, searchString,dateFROM,dateTO):
        print(searchString) # e.g. halloIch bin ein Suchstring
        print(dateFROM) # e.g. Tue Jan 08 2019 12:00:00 GMT+0100 (Central European Standard Time) # wenn nicht vorhanden: None
        print(dateTO) # e.g. Tue Jan 08 2019 12:00:00 GMT+0100 (Central European Standard Time)
        
        
        
        # data muss eine liste / Array sein (kann geändert werden, erfordert aber eine Änderung im Backend)
        data = search.get_search_results(searchString)
        print(data)
        print(type(data))
        #print(type(data[0]))
        

        
        
        # der return sollte vielleicht auf maximal 20 Elemente beschränkt sein
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, default=json_util.default)


def main():
    s = zerorpc.Server(GetSearchResultsRPC())
    s.bind("tcp://*:4242")
    s.run()

if __name__ == "__main__" : main()
