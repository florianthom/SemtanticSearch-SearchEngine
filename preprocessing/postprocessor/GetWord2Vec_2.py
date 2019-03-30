import gensim

class GetWord2Vec:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load("wiki.model", mmap="r")

    def getword2vec(self,search_term):
        text = search_term
        listword = text.split(' ')
        dictneu = {}
        for w in listword:
            try:
                dictneu[w]=self.model.most_similar (positive=w,topn=3)
            except Exception as exception:
                pass
        return dictneu

    def getModel(self):
        return self.model
   
    '''
    Ideen fuer entsprechende zusaetzliche Inhalte 

    model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
    [('queen', 0.50882536)]
    model.doesnt_match("breakfast cereal dinner lunch";.split())
    'cereal'
    model.similarity('woman', 'man')
    0.73723527
    '''