import gensim
from gensim.models import Word2Vec

class GetWord2Vec:
    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format("german.model", binary=True)

    def getword2vec(self,search_term):
        text = self.replace_german_umlaute(search_term)
        listword = text.split(' ')
        dictneu = {}
        for w in listword:
            try:
                dictneu[w]=self.model.most_similar (positive=w)
            except Exception as exception:
                pass
        return dictneu

    def replace_german_umlaute(self,string_text):
        chars = {'ö':'oe','Ö':'Oe','Ä':'Ae','ä':'ae','Ü':'Ue','ü':'ue','ß':'ss'} # usw.
        for char in chars:
            string_text = string_text.replace(char,chars[char])
        return string_text