import random
import pickle

import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from pymongo import MongoClient
import json
from bson import json_util

from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger

class Preprocessor:
    def __init__(self):
        self.stemmer_german = SnowballStemmer('german')
        with open('nltk_german_classifier_data.pickle', 'rb') as f:
        #Lade den neuen alten Tagger in eine neue Instanz
            self.tagger = pickle.load(f)
        self.stop_words = stopwords.words('german')

        self.umlaute_dict = {
            '\xc3\xa4': 'ae',  # U+00E4	   \xc3\xa4
            '\xc3\xb6': 'oe',  # U+00F6	   \xc3\xb6
            '\xc3\xbc': 'ue',  # U+00FC	   \xc3\xbc
            '\xc3\x84': 'Ae',  # U+00C4	   \xc3\x84
            '\xc3\x96': 'Oe',  # U+00D6	   \xc3\x96
            '\xc3\x9c': 'Ue',  # U+00DC	   \xc3\x9c
            '\xc3\x9f': 'ss',  # U+00DF	   \xc3\x9f
        }

    def replace_german_umlaute(self,unicode_string):
        utf8_string = unicode_string.encode('utf-8')
        for k in self.umlaute_dict.keys():
            utf8_string = utf8_string.replace(k, self.umlaute_dict[k])
        return utf8_string.decode()

    def tokenizing_with_sw_and_punc(self,text):
        text = text.lower()
        # tokenize text 
        return word_tokenize(text)
        
    def tokenizing_without_punc(self,text):
        tokenizer = RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(text)

    def tokenizing_complete(self,text):
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in self.stop_words:#
                #str(self.replace_german_umlaute(w))
                filtered_sentence.append(w)
        filtered_word_tokens = filtered_sentence
        return filtered_word_tokens


    def tokenizing_reverse(self,words):
        return nltk.Text(words)

    def stemming(self,word):
        return self.stemmer_german.stem(word)

    def stemming_words(self,word_tokens):
        stemmed_tokens = []
        for w in word_tokens:
            stemmed_tokens.append(self.stemmer_german.stem(w))
        return stemmed_tokens

    def lemmating(self,words):
        return self.tagger.tag(words)

   

    

