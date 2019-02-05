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

# Extract word vectors
#word_embeddings = {}
#f = open('glove.6B.100d.txt', encoding='utf-8')
#for line in f:
#    values = line.split()
#    word = values[0]
#    coefs = np.asarray(values[1:], dtype='float32')
#    word_embeddings[word] = coefs
#f.close()

#print(len(word_embeddings))

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
    for i in range(2):
      print(ranked_sentences[i][1])