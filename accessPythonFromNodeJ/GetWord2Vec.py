import gensim

class GetWord2Vec:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load("word2vec.model", mmap="r")

    def getword2vec(self,search_term):
        text = search_term
        listword = text.split(' ')
        dictneu = {}
        for w in listword:
            try:
                dictneu[w]=self.model.most_similar (positive=w)
            except Exception as exception:
                pass
        return dictneu
