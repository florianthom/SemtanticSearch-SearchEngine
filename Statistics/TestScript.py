from Statistics import Statistics
from pymongo import MongoClient
from bson.objectid import ObjectId

"""
Kurzbeschreibung:

Hier werden alle funktionen mal aufgerufen um zu zeigen wie sie
wenn Statistics mit der Flag 'set_dummy_data=True' aufgerufen wird
werden paar dummy daten in die db geschrieben, damit man schon mal Suchergebnisse bekommt.

Wenn die 'printflag=True' gesetzt wird bedeutet das lediglich dass man bisschen output bekommt
wenn die Funktionen aufgerufen werden.

    write_search_term_to_db: Schreibt einen string in die DB und setzt den count auf 1
    bzw erhöt den count um 1 wenn das wort schon bekannt ist.
    
    get_top_search_terms: Gibt eine Liste der top gesuchen wörter zurück und die Anzahl 
    der Suchen.
    
    write_read_articles_to_db: Macht dasselbe wie write_search_term_to_db nur für Suchergebnisse. 
    Hier werden die ObjectIds der gecrawlten Artikel in einer Liste übergeben.
    
    get_top_read_articles: Gibt die ObjectIds der top 3 Suchtreffer zurück und deren Count in einer Liste.
    
"""

# Set!!!!!
client = MongoClient('localhost', 27017)
# Set!!!!!
db = client.test

stat = Statistics(set_dummy_data=True)

print()
print('Write a search term to db', '#' * 30)
stat.write_search_term_to_db("new_term1", printflag=True)
stat.write_search_term_to_db("new_term1", printflag=True)
stat.write_search_term_to_db("new_term2", printflag=True)
print('End of term to db', '#' * 30)
print()

print('Get top search terms', '#' * 30)
stat.get_top_search_terms(printflag=True)
print('End of term to db', '#' * 30)
print()

print('Write search results to db', '#' * 30)
myList = ['ObjectId1', 'ObjectId2', 'ObjectId3']
stat.write_read_articles_to_db(myList, printflag=True)
myList = ['ObjectId1', 'ObjectId2']
stat.write_read_articles_to_db(myList, printflag=True)
myList = ['ObjectId1']
stat.write_read_articles_to_db(myList, printflag=True)
print('End of result to db', '#' * 30)
print()

print('Get top search results', '#' * 30)
stat.get_top_read_articles(printflag=True)
print('End of top search results', '#' * 30)
