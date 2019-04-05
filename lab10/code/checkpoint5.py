#!/usr/bin/env python
from pymongo import MongoClient
import pprint
import datetime
import random
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.mongo_db_lab
    collection = db.definitions

    ind = random.randint(0, collection.count() )
    random_word = list(collection.find())[ind]

    collection.update_one(\
            {"word": random_word["word"]}, \
            {"$push": {"dates": datetime.datetime.now()} } )

    return random_word


if __name__ == '__main__':
    print (random_word_requester())
