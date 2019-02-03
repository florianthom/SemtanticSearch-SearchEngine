import spacy
nlp = spacy.load("de")

class PreprocessorSpacy:
    def replace_german_umlaute(self,string_text):
        chars = {'ö':'oe','Ö':'Oe','Ä':'Ae','ä':'ae','Ü':'Ue','ü':'ue','ß':'ss'} # usw.
        for char in chars:
            string_text = string_text.replace(char,chars[char])
        return string_text

    def tokenizing_with_sw_and_punc(self, text):
        text = self.replace_german_umlaute(text)
        # tokenize text
        return [token.text for token in nlp(text)]

    def tokenizing_without_punc(self, text):
        tokenizer = [token.text for token in nlp(text) if token.is_punct != True]
        return self.replace_german_umlaute(self.tokenizing_reverse(tokenizer))

    def tokenizing_without_punc_and_sw_with_umlaute(self, text):
        return[ token.text for token in nlp(text) if token.is_punct != True and token.is_stop != True]

    def tokenizing_without_punc_with_umlaute_sw(self, text):
        return [ token.text for token in nlp(text) if token.is_punct != True]

    def tokenizing_complete(self, text):
        tokenizer = [ token.text for token in nlp(text) if token.is_punct != True and token.is_stop != True]
        return self.replace_german_umlaute(self.tokenizing_reverse(tokenizer))

    def tokenizing_reverse(self, words):
        return ' '.join(words)#nltk.Text(words)

    def stemming_words(self, word_tokens):
        pass

    def lemmating(self, words):
        return [token.lemma_ for token in nlp(words)]
