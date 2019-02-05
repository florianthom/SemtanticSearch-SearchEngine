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
import sklearn.metrics.pairwise as sklearnPairwise
from scipy.sparse import hstack,vstack
from scipy.sparse import csr_matrix
import GetWord2Vec

class Search():

    connectionDatabaseMongo = None
    
    def __init__(self,connectionDatabaseMongo):
        self.connectionDatabaseMongo = connectionDatabaseMongo
        global collection_working_data
        collection_working_data = self.connectionDatabaseMongo.lower_without_punctuation_with_SW # work-data
        global collection_raw_data
        collection_raw_data = self.connectionDatabaseMongo.crawlerdb # raw-data
        global collection_inverse_index
        collection_inverse_index = self.connectionDatabaseMongo.crawlerdb_INVERSE_INDEX # raw-data
        global preprocessor
        preprocessor = Preprocessor.Preprocessor()
        global result_dict_with_ids
        global tfidf
        global tfidf_values
        global preprocessor
        preprocessor = Preprocessor.Preprocessor()
        getword2vec = GetWord2Vec.GetWord2Vec()

        
        #calculate initial tf-idf vectors
        result_documents_list_REAL = list(collection_working_data.find({})) # find returns cursor, like an iterator in scala
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
        
        # finished pre TF_IDF - Calculation here
        
        
    def get_search_results(self,search_term = "zwei maskierte männer haben heute"):
        tokenized_words = preprocessor.tokenizing_without_punc(search_term)
        stemmed_search_term = preprocessor.stemming_words(tokenized_words)
        
	# transform search-term to tf-idf vektor (without fit -> only transform)
        tfidf_search_term = tfidf.transform([search_term]) # transform passt idf nicht an
        

        result_list_from_inverse_index = collection_inverse_index.find({"word": {"$in": tokenized_words}}) ######################################################### tokenized und nicht stemmed
        
#        # combine result ids from inverse index with in a set via intersection
#        try:
#                result_ids = set(result_list_from_inverse_index[0]["documents"])
#                for i in result_list_from_inverse_index:
#                        result_ids = result_ids.intersection(i["documents"])
#        except IndexError:
#                result_ids = set()


        # combine result ids from inverse index with in a set via union
        test1 = collection_inverse_index.find({"word": {"$in": tokenized_words}})
        result_ids = set()
        for i in test1:
                result_ids.update(i["documents"])

        #unpack result_dict_with_ids: now we need only den Dokumentenvektor
        if(result_ids != set()):
        	less_document_actually= matrix = vstack([result_dict_with_ids[i] for i in result_ids])
        else:
                return []



        #calculate cos_sim
        cos_sim_results = sklearnPairwise.cosine_similarity(X=matrix,Y=tfidf_search_term).reshape(-1)

        # now we need the id to the cos-sim-vectors again and the cos-sim itself (together in a dict)
        new_ids_with_scores = {}
        i = 0
        for a in result_ids:
            new_ids_with_scores[a] = cos_sim_results[i]
            i+=1

        # sort by cos-sim and return the first 20 elements
        sorted_d = sorted(new_ids_with_scores.items(), key=operator.itemgetter(1), reverse=True)[0:20]
        ids = [ObjectId(sorted_d[i][0]) for i in range(len(sorted_d))]

        documents = collection_raw_data.find({"_id" : {"$in" : ids}})

        # attach a new field to the data: "cossim"
        # this field stores the cossim-result
        list_of_documents = list(documents)
        for i in range(len(list_of_documents)):
            list_of_documents[i]["cossim"] = sorted_d[i][1]
        return list_of_documents
