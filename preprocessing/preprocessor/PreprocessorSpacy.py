import spacy
nlp = spacy.load("de")

def replace_german_umlaute(string_text):
    chars = {'ö':'oe','Ö':'Oe','Ä':'Ae','ä':'ae','Ü':'Ue','ü':'ue','ß':'ss'} # usw.
    for char in chars:
        string_text = string_text.replace(char,chars[char])
    return string_text

def tokenizing_with_sw_and_punc(text):
    text = self.replace_german_umlaute(text.lower())
    # tokenize text
    return [token.text for token in nlp(text)]

def tokenizing_without_punc(text):
    tokenizer = [ token.text for token in nlp(text) if token.is_punct != True]
    return tokenizer.tokenize(self.replace_german_umlaute(text.lower()))

def tokenizing_without_punc_and_sw_with_umlaute(text):
    tokenizer = [ token.text for token in nlp(text) if token.is_punct != True and token.is_stop != True]
    word_tokens = tokenizer.tokenize(text.lower())
    return word_tokens

def tokenizing_without_punc_with_umlaute_sw(text):
    tokenizer = [ token.text for token in nlp(text) if token.is_punct != True]
    return tokenizer.tokenize(text.lower())

def tokenizing_complete(text):
    tokenizer = [ token.text for token in nlp(text) if token.is_punct != True and token.is_stop != True]
    word_tokens = tokenizer.tokenize(text)
    filtered_word_tokens = self.replace_german_umlaute(text.lower())
    return filtered_word_tokens

def tokenizing_reverse(words):
    return ' '.join(words)#nltk.Text(words)

def stemming_words(word_tokens):
    pass

def lemmating(words):
    return return [token.lemma_ for token in nlp(words)]
