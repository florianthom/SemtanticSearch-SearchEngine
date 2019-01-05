import zerorpc
from pymongo import MongoClient
import json
from bson import json_util
#from bson import json_util



class GetSearchResultsRPC(object):
    
    client= None
    db = None
    collection = None
    
    def __init__(self):
        print("constructor")
        self.client = MongoClient("127.0.0.1:27017")
        self.db = client.crawlerdb
        self.collection = db.crawlerdb
        
        
    def get_results(self, searchString):
        data = self.collection.find({})[0]
        print(searchString)
        # anstatt die json zu returnen, könnte man auch nur die IDs returnen und die Json von node.js aus fetchen
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, default=json_util.default)

    
def main():
    s = zerorpc.Server(GetSearchResultsRPC())
    s.bind("tcp://*:4242")
    s.run()

if __name__ == "__main__" : main()
