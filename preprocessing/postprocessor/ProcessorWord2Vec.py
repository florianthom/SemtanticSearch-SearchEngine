import gensim
from gensim.models import Word2Vec

class ProcessWord2Vec:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format("german.model", binary=True)

    def synonyms_from_german_corpus_word2vec(self,search_term):
        listword = search_term.split(' ')
        dictneu = {}
        for w in listword:
            try:
                dictneu[w]=self.model.most_similar (positive=w)
            except Exception as exception:
                #exception.with_traceback
                pass
        return dictneu