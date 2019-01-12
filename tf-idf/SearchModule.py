# NEEDS: Database and in that DB: 2 Collections: 1. crawlerdb_lower_withSW 2. crawlerdb_INVERSE_INDEX

import numpy as np
import nltk
from nltk.text import TextCollection
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from numpy import dot
from numpy.linalg import norm
import Preprocessor
from bson import ObjectId
import operator

class Search():

    connectionDatabaseMongo = None
    
    def __init__(self,connectionDatabaseMongo):
        self.connectionDatabaseMongo = connectionDatabaseMongo
        global collection
        collection = self.connectionDatabaseMongo.crawlerdb_lower_withSW
        global preprocessor
        preprocessor = Preprocessor.Preprocessor()
        global result_dict_with_ids
        global tfidf
        global tfidf_values
        
        #calculate initial tf-idf vectors
        result_documents_list_REAL = list(collection.find({})) # find returns cursor, like an iterator in scala
        print("We got ", len(result_documents_list_REAL), " Documents")
        
        #result_document_text_list = [a["text"] for a in result_documents_list_REAL] # wir müssen erst result_documents_list["text"] "entpacken" von cursor
        result_document_text_list = list()
        for i in range(len(result_documents_list_REAL)):
            try:
                result_document_text_list.append(result_documents_list_REAL[i]["text"]) # Fehler: KeyError: muss abgefangen werden
            except KeyError:
                pass
        print("We still have ", len(result_document_text_list), " Documents")
        
        
        tfidf = TfidfVectorizer()
        tfidf_values = tfidf.fit_transform(result_document_text_list) # output= <class 'scipy.sparse.csr.csr_matrix'>
        
        result_dict_with_ids = {}
        for i in range(len(result_documents_list_REAL)):
            key = str(result_documents_list_REAL[i]["_id"]) # 5c2fb3c988df422822370767
            result_dict_with_ids[key] = tfidf_values[i]
        print("test for: result_dict_with_ids", result_dict_with_ids["5c2fb3c988df422822370767"])
        
        # finished pre TF_IDF - Calculation here
        
        
    def get_search_results(self,search_term = "zwei maskierte männer haben heute"):
        preprocessor = Preprocessor.Preprocessor()
        tokenized_words = preprocessor.tokenizing_without_punc(search_term)
        stemmed_search_term = preprocessor.stemming_words(tokenized_words)

        # get all important documents from db
        result_ids = set()
        collection_inverse_index = self.connectionDatabaseMongo.crawlerdb_INVERSE_INDEX
        for i in stemmed_search_term:
            print(i)
            record = collection_inverse_index.find({"word": i})
            ids_in_tupel_now_in_list = list() # ["sadfasdf", "sadfsda", ...]
            for m in record:
                current = list(m["documents"]) # ["asdfsadf"]
                for a in current:
                    result_ids.add(a)


        #unpack result_dict_with_ids: now we need only den Dokumentenvektor
        less_document_actually = list()
        for i in result_ids:
            less_document_actually.append(result_dict_with_ids[i])

        # transform search-term to tf-idf vektor (without fit -> only transform)
        tfidf_search_term = tfidf.transform([search_term]) # transform passt idf nicht an

        # now we dont need sparse-representation of the vectors in "less_document_actually" but the dense-vectors
        less_documents = list()
        for a in range(len(less_document_actually)):
            less_documents.append(less_document_actually[a].toarray().reshape(-1))
        print("We have the following number of important selected documents for example from inverse index: ", len(less_documents))


        # speichern der cos-sim-results
        cos_sim_results = list()
        #calculation of the cos-sim
        for i in range(len(less_documents)): # actually all values in tfidf_values.todense().shape[0] but that is not possible
                #aufpassen: search term was array now its a string
            tfidf_values_tmp = less_documents[i]
            tfidf_search_term_tmp = np.array(tfidf_search_term.todense()).reshape(-1)

            first = np.dot(tfidf_values_tmp, tfidf_search_term_tmp)
            second = (norm(tfidf_values_tmp)*norm(tfidf_search_term_tmp))
            cos_sim = first * 1.0/second
            cos_sim_results.append(cos_sim)
            #print("cos sim of the current - document with the search-string is: ",cos_sim)

        # now we need the id to the cos-sim-vectors again and the cos-sim itself (together in a dict)
        new_ids_with_scores = {}
        i = 0
        for a in result_ids:
            new_ids_with_scores[a] = cos_sim_results[i]
            i+=1

        # sort by cos-sim and return the first 20 elements
        sorted_d = sorted(new_ids_with_scores.items(), key=operator.itemgetter(1), reverse=True)[0:20]
        ids = [ObjectId(sorted_d[i][0]) for i in range(len(sorted_d))]

        documents = collection.find({"_id" : {"$in" : ids}})

        # attach a new field to the data: "cossim"
        # this field stores the cossim-result
        list_of_documents = list(documents)
        for i in range(len(list_of_documents)):
            list_of_documents[i]["cossim"] = sorted_d[i][1]
        return list_of_documents