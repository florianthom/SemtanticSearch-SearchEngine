import Preprocessor
import collections
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

import numpy as np
import pandas as pd
import nltk
nltk.download('punkt') # one time execution
import re
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

from nltk import tokenize

def unpackAndSummarize(data, word_embeddings):
    embeddings = word_embeddings
    for document in data:  
        text = document.get("text")
        summary = textRank(text, embeddings)
        document['summary'] = summary
    

def textRank(text, word_embeddings):
    preprocessor = Preprocessor.Preprocessor()
    text = " ".join(text.split())
    sentence_list = tokenize.sent_tokenize(text) 
    word_list = preprocessor.tokenizing_without_punc(text)
    
    sentence_vectors = []
    for i in sentence_list:
      if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
      else:
        v = np.zeros((100,))
      sentence_vectors.append(v)
    
    # similarity matrix
    sim_mat = np.zeros([len(sentence_list), len(sentence_list)])
    for i in range(len(sentence_list)):
      for j in range(len(sentence_list)):
        if i != j:
          sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentence_list)), reverse=True)
    # Extract top 10 sentences as the summary
    summary = []
    for i in range(2):
      summary.append(ranked_sentences[i][1])
    s = ''.join(summary)
    return s