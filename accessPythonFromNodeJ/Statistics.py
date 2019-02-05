from pymongo import MongoClient
from bson.objectid import ObjectId


class Statistics:
    """Provides methods to create staistical data for search terms.

    Functions:
        write_search_term_to_db(): Writes search term to db / udpates its search count.
        Collection: 'words'
        get_top_search_terms(): Returns list of top searched for terms and their counts.

        write_search_results_to_db(): Writes search results to db / udpates its search count.
        Collection: 'read_articles'
        get_top_search_results(): Returns list of top results and their counts.

    """

    def __init__(self, set_dummy_data=False):
        """
        MongoClient will be set in constructer.
        If set_dummy_data is set to True, some data will be
        written to db.

        :param set_dummy_data:
        """
        # Set!!!!!
        self.client = MongoClient('localhost', 27017)
        # Set!!!!!
        self.db = self.client.statistics
        if set_dummy_data:
            # Insert dummy values
            self.fill_with_dummy_data()
            print("Success writing dummy data to db")

    def write_search_term_to_db(self, search_term, printflag=False):
        """Function that writes a search term to the database

        Writes a search term to the database collection 'words' and
        updates the 'count' attribute if the term already exists in
        database.
        If the printflag ist set to True, the progress will be printed
        to terminal.

        Structure in db:

        {
          "_id": "5c430756a9bdf01d60fb0850",
          "word": "test0",
          "count": 2
        }

        :param search_term: The term to write to db
        :param printflag: Specifies if progress should be printed
        :return: None
        """
        try:
            item = self.db.words.find_one({'word': search_term})
            # If word is already in db
            if item:
                # Update 'count' value
                new_count = item.get('count') + 1
                self.db.words.update({"word": search_term}, {'$set': {"count": new_count}})
                if printflag:
                    print("Word updated")
            else:
                # Else initialise word in db
                self.db.words.insert({'word': search_term, 'count': 1})
                if printflag:
                    print("Word initialised")
        except:
            print("Writing to db didn't work")

    def get_top_search_terms(self, printflag=False):
        """Function to return the top searched for terms

        This function returns a list containing the word
        and it's count for the three most searched words.
        Returns an empty list if function failed.

        Format of list:
            [['word', count], ['word', count], ['word', count]]

        :param printflag: Specifies if progress should be printed
        :return: Returns the list of top searched for words
        """
        try:
            results = self.db.words.find().sort([("count", -1)]).limit(3)
            return_list = []
            for item in results:
                word = item.get('word')
                count = item.get('count')
                return_list.append([word, count])
            if printflag:
                print("Success getting top search terms")
                print("Result:")
                print(return_list)
            return return_list
        except:
            print("Getting top search terms didn't work")
            return return_list

    def fill_with_dummy_data(self):
        """Fills db with dummy data.

        This function is only used in constructor if
        flag is set.
        Only writes data to db if the words are not already set.

        :return: None
        """
        try:
            item = self.db.words.find_one({'word': 'Haus'})
            if item is None:
                self.db.words.insert({'word': "Haus", 'count': 3})
            item2 = self.db.words.find_one({'word': 'Polizei'})
            if item2 is None:
                self.db.words.insert({'word': "Polizei", 'count': 2})
            item3 = self.db.words.find_one({'word': 'Einbruch'})
            if item3 is None:
                self.db.words.insert({'word': "Einbruch", 'count': 1})
        except:
            print("Setting dummy values failed")

    def write_read_articles_to_db(self, results_object_ids, printflag=False):
        """Function that writes a search result to the database

        Writes a search result to the database collection 'read_articles' and
        updates the 'count' attribute if the result already exists in
        database.
        If the printflag ist set to True, the progress will be printed
        to terminal.

        Structure in db:
        {
          "_id": "5c4306ada9bdf0022c19c9d1",
          "result_id": "Polizei",
          "count": 1
        }

        :param results_object_ids: List of object ids
        :param printflag: Specifies if progress should be printed
        :return: None
        """
        try:
            for obj_id in results_object_ids:
                try:
                    item = self.db.read_articles.find_one({"result_id": obj_id})
                    # If Result is already in db
                    if item:
                        # Update 'count' value
                        new_count = item.get('count') + 1
                        self.db.read_articles.update({"result_id": obj_id}, {'$set': {"count": new_count}})
                        if printflag:
                            print(obj_id, "Result updated")
                    else:
                        # Else initialise word in db
                        self.db.read_articles.insert({"result_id": obj_id, 'count': 1})
                        if printflag:
                            print(obj_id, "Result initialised")
                except:
                    print("Writing to db didn't work")
        except:
            print("For loop failed when writing search results to db")

    def get_top_read_articles(self, printflag=False):
        """Function to return the top read articles

        This function returns a list containing the object id's of top 3 read articles
        and it's count for the three most searched search results.
        Returns an empty list if function failed.

        Format of list:
            [[object_id, count], [object_id, count], [object_id, count]]

        :param printflag: Specifies if progress should be printed
        :return: Returns the list of top searched for words
        """
        try:
            results = self.db.read_articles.find().sort([("count", -1)]).limit(3)
            return_list = []
            for item in results:
                word = item.get('result_id')
                count = item.get('count')
                return_list.append([word, count])
            if printflag:
                print("Success getting top search results")
                print("Result:")
                print(return_list)
            return return_list
        except:
            print("Getting top search result didn't work")
            return return_list
