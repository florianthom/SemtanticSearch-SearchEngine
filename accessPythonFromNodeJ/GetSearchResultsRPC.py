import zerorpc
from pymongo import MongoClient
import json
from bson import json_util
#from bson import json_util



class GetSearchResultsRPC(object):
    
    '''pass the method a name, it replies "Hello name!"'''
    def get_results(self, parameter1):
        client = MongoClient("127.0.0.1:27017")
        db=client.crawlerdb # crawl_database_1 is the db name
        collection = db.crawlerdb
        data = [collection.find({})[0]]
        print(type(parameter1))
        print(parameter1)
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, default=json_util.default)



def main():
    s = zerorpc.Server(GetSearchResultsRPC())
    s.bind("tcp://*:4242")
    s.run()

if __name__ == "__main__" : main()

# node.js client:

#var zerorpc = require("zerorpc");

#var client = new zerorpc.Client();
#client.connect("tcp://127.0.0.1:4242");
#//calls the method on the python object
#client.invoke("hello", "World", function(error, reply, streaming) {
#    if(error){
#        console.log("ERROR: ", error);
#    }
#    console.log(reply);
#});
