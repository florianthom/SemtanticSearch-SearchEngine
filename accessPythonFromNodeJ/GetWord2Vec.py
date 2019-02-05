import gensim
from gensim.models import Word2Vec

class GetWord2Vec:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format("german.model", binary=True)

    def getword2vec(self,search_term):
        listword = search_term.split(' ')
        dictneu = {}
        for w in listword:
            try:
                dictneu[w]=self.model.most_similar (positive=w)
            except Exception as exception:
                pass
        return dictneu