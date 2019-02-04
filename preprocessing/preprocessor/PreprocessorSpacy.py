import spacy
nlp = spacy.load("de")

def replace_german_umlaute(string_text):
    chars = {'ö':'oe','Ö':'Oe','Ä':'Ae','ä':'ae','Ü':'Ue','ü':'ue','ß':'ss'} # usw.
    for char in chars:
        string_text = string_text.replace(char,chars[char])
    return string_text

def tokenizing_with_sw_and_punc(text):
    text = replace_german_umlaute(text.lower())
    return [token.text for token in nlp(text)]

def tokenizing_without_punc(text):
    text = replace_german_umlaute(text.lower())
    return[token.text for token in nlp(text) if token.is_punct != True]

def tokenizing_without_punc_and_sw_with_umlaute(text):
    return[ token.text for token in nlp(text.lower()) if token.is_punct != True and token.is_stop != True]

def tokenizing_without_punc_with_umlaute_sw(text):
    return [ token.text for token in nlp(text.lower()) if token.is_punct != True]

def tokenizing_complete(text):
    text = replace_german_umlaute(text)
    return [token.text for token in nlp(text.lower()) if token.is_punct != True and token.is_stop != True]

def tokenizing_reverse(words):
    return ' '.join(words)#nltk.Text(words)

def stemming(word):
    pass

def stemming_words(word_tokens):
    pass

def lemmating(words):
    words = tokenizing_reverse(words)
    return [token.lemma_ for token in nlp(words)]