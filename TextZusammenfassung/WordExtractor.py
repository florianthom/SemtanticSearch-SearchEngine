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

def extractWordembeddings():
   # Extract word vectors
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()
    return word_embeddings