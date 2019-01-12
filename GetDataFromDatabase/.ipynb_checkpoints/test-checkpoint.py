import numpy as np
import nltk
from nltk.text import TextCollection
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from numpy import dot
from numpy.linalg import norm

client = MongoClient("localhost")
db=client.crawlerdb_WORK_TFIDF_2
collection = db.crawlerdb_lower_withSW
result_documents_list_REAL = list(collection.find({})) # find returns cursor, like an iterator in scala
print("We got ", len(result_documents_list_REAL), " Documents")

result_documents_list = [{'_id': '5c2b861a7faca327135730a6',
  'date': '27.06.2017',
  'title': 'Ein Schwerverletzter und zwei Leichtverletzte bei Auseinandersetzung',
  'location': 'Mitte',
  'text': 'hallo hier bin In der Nacht kam es in Mitte zu einer Auseinandersetzung zwischen mehreren Personen, bei der drei Männer verletzt wurden. Ersten Ermittlungen zufolge sollen sich die drei Verletzten, im Alter von 18, 20 und 21 Jahren, gemeinsam mit Freunden und ihnen Unbekannten gegen Mitternacht am Neptunbrunnen in der Spandauer Straße aufgehalten haben. Plötzlich habe ein Unbekannter eine Glasfasche geworfen, die jedoch niemanden traf. Daraufhin sei es zu einem Handgemenge gekommen, in dessen Verlauf zwei Männer Reizgas versprühten. Die beiden 18 und 20 Jahre alten Männer erlitten leichte Augenreizungen, die zum Teil ambulant von alarmierten Rettungskräften behandelt wurden. Im Zuge der Anzeigenaufnahme erfuhren die Beamten, dass unter der Liebknechtbrücke der 21-Jährige liege, der eine Schnittwunde aufwies. Diese habe er von einem ihm namentlich nicht bekannten Mann im Anschluss an das Handgemenge mit einem Messer zugefügt bekommen. Rettungskräfte brachten den Schwerverletzten zur\n    stationären Behandlung in eine Klinik. Die genauen Hintergründe der Tat sind nun Teil der Ermittlungen, die die Kriminalpolizei der Direktion 3 führt.',
  'number': ['Nr. 1431', '']},
 {'_id': '5c2b861a7faca327135730a7',
  'date': '17.07.2017',
  'title': 'Ein Krankenwagenunfall',
  'location': 'Osten',
  'text': 'hallo Während des Tages kam es in Mitte zu einer Auseinandersetzung zwischen mehreren Personen, bei der drei Männer verletzt wurden. Ersten Ermittlungen zufolge sollen sich die drei Verletzten, im Alter von 18, 20 und 21 Jahren, gemeinsam mit Freunden und ihnen Unbekannten gegen Mitternacht am Neptunbrunnen in der Spandauer Straße aufgehalten haben. Plötzlich habe ein Unbekannter eine Glasfasche geworfen, die jedoch niemanden traf. Daraufhin sei es zu einem Handgemenge gekommen, in dessen Verlauf zwei Männer Reizgas versprühten. Die beiden 18 und 20 Jahre alten Männer erlitten leichte Augenreizungen, die zum Teil ambulant von alarmierten Rettungskräften behandelt wurden. Im Zuge der Anzeigenaufnahme erfuhren die Beamten, dass unter der Liebknechtbrücke der 21-Jährige liege, der eine Schnittwunde aufwies. Diese habe er von einem ihm namentlich nicht bekannten Mann im Anschluss an das Handgemenge mit einem Messer zugefügt bekommen. Rettungskräfte brachten den Schwerverletzten zur\n    stationären Behandlung in eine Klinik. Die genauen Hintergründe der Tat sind nun Teil der Ermittlungen, die die Kriminalpolizei der Direktion 3 führt.',
  'number': ['Nr. 1430', '']},
 {'_id': '5c2b861a7faca327135730a8',
  'date': '16.07.2017',
  'title': 'Feuer in einem Haus',
  'location': 'Westen',
  'text': 'hier Während des Tages kam es in Mitte zu einem Konflikt zwischen mehreren Personen, bei der drei Männer verletzt wurden. Ersten Ermittlungen zufolge sollen sich die drei Verletzten, im Alter von 18, 20 und 21 Jahren, gemeinsam mit Freunden und ihnen Unbekannten gegen Mitternacht am Neptunbrunnen in der Spandauer Straße aufgehalten haben. Plötzlich habe ein Unbekannter eine Glasfasche geworfen, die jedoch niemanden traf. Daraufhin sei es zu einem Handgemenge gekommen, in dessen Verlauf zwei Männer Reizgas versprühten. Die beiden 18 und 20 Jahre alten Männer erlitten leichte Augenreizungen, die zum Teil ambulant von alarmierten Rettungskräften behandelt wurden. Im Zuge der Anzeigenaufnahme erfuhren die Beamten, dass unter der Liebknechtbrücke der 21-Jährige liege, der eine Schnittwunde aufwies. Diese habe er von einem ihm namentlich nicht bekannten Mann im Anschluss an das Handgemenge mit einem Messer zugefügt bekommen. Rettungskräfte brachten den Schwerverletzten zur\n    stationären Behandlung in eine Klinik. Die genauen Hintergründe der Tat sind nun Teil der Ermittlungen, die die Kriminalpolizei der Direktion 3 führt.',
  'number': ['Nr. 1432', '1430']},
 {'_id': '5c2b861a7faca327135730a9',
  'date': '17.07.2017',
  'title': 'Feuer in einem Haus',
  'location': 'Westen',
  'text': 'bin Während des Tages kam es in Mitte zu einem Konflikt zwischen einer Person, bei der 4 Männer verletzt wurden. Ersten Ermittlungen zufolge sollen sich die drei Verletzten, im Alter von 18, 20 und 21 Jahren, gemeinsam mit Freunden und ihnen Unbekannten gegen Mitternacht am Neptunbrunnen in der Spandauer Straße aufgehalten haben. Plötzlich habe ein Unbekannter eine Glasfasche geworfen, die jedoch niemanden traf. Daraufhin sei es zu einem Handgemenge gekommen, in dessen Verlauf zwei Männer Reizgas versprühten. Die beiden 18 und 20 Jahre alten Männer erlitten leichte Augenreizungen, die zum Teil ambulant von alarmierten Rettungskräften behandelt wurden. Im Zuge der Anzeigenaufnahme erfuhren die Beamten, dass unter der Liebknechtbrücke der 21-Jährige liege, der eine Schnittwunde aufwies. Diese habe er von einem ihm namentlich nicht bekannten Mann im Anschluss an das Handgemenge mit einem Messer zugefügt bekommen. Rettungskräfte brachten den Schwerverletzten zur\n    stationären Behandlung in eine Klinik. Die genauen Hintergründe der Tat sind nun Teil der Ermittlungen, die die Kriminalpolizei der Direktion 3 führt.',
  'number': ['Nr. 1428', '']},
 {'_id': '5c2b861a7faca327135730aa',
  'date': '15.07.2017',
  'title': 'Feuer in einem Haus',
  'location': 'Norden',
  'text': 'ich Während des Tages kam es in Mitte zu einem Konflikt zwischen einer Person, bei der 4 Männer verwunded wurden. Ersten Ermittlungen zufolge sollen sich die drei Verletzten, im Alter von 18, 20 und 21 Jahren, gemeinsam mit Freunden und ihnen Unbekannten gegen Mitternacht am Neptunbrunnen in der Spandauer Straße aufgehalten haben. Plötzlich habe ein Unbekannter eine Glasfasche geworfen, die jedoch niemanden traf. Daraufhin sei es zu einem Handgemenge gekommen, in dessen Verlauf zwei Männer Reizgas versprühten. Die beiden 18 und 20 Jahre alten Männer erlitten leichte Augenreizungen, die zum Teil ambulant von alarmierten Rettungskräften behandelt wurden. Im Zuge der Anzeigenaufnahme erfuhren die Beamten, dass unter der Liebknechtbrücke der 21-Jährige liege, der eine Schnittwunde aufwies. Diese habe er von einem ihm namentlich nicht bekannten Mann im Anschluss an das Handgemenge mit einem Messer zugefügt bekommen. Rettungskräfte brachten den Schwerverletzten zur\n    stationären Behandlung in eine Klinik. Die genauen Hintergründe der Tat sind nun Teil der Ermittlungen, die die Kriminalpolizei der Direktion 3 führt.',
  'number': ['Nr. 1427', '']}]

#result_document_text_list = [a["text"] for a in result_documents_list_REAL] # wir müssen erst result_documents_list["text"] "entpacken" von cursor
result_document_text_list = list()
for i in range(len(result_documents_list_REAL)):
    try:
        result_document_text_list.append(result_documents_list_REAL[i]["text"]) # Fehler: KeyError: muss abgefangen werden
    except KeyError:
        pass
    
print("We still have ", len(result_document_text_list), " Documents")

search_term = ["hallo hier bin ich"]

tfidf = TfidfVectorizer()
tfidf_values = tfidf.fit_transform(result_document_text_list)
#pd.DataFrame(tfidf_values.todense(),columns=tfidf.get_feature_names())
print("We have ", tfidf_values.todense().shape[0], "vectors")


type(tfidf_values)

tfidf_search_term = tfidf.transform(search_term) # transform passt idf nicht an
#tfidf_search_term.todense()

for i in range(tfidf_values.shape[0]):
    tfidf_values_tmp = np.array(tfidf_values.todense()[i]).reshape(-1)
    tfidf_search_term_tmp = np.array(tfidf_search_term.todense()).reshape(-1)
    
    first = np.dot(tfidf_values_tmp, tfidf_search_term_tmp)
    second = (norm(tfidf_values_tmp)*norm(tfidf_search_term_tmp))
    cos_sim = first * 1.0/second
    print(cos_sim)