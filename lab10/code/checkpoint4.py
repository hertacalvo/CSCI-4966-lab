#!/usr/bin/env python 
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient()

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    db = client.mongo_db_lab
    collection = db.definitions
    # Getting all items
    print("\n{}\n** Finding all items\n{}\n".format("*"*55, "*"*55))
    pp.pprint(list(collection.find()))
    # Getting one item
    print("\n{}\n** Finding a single item\n{}\n".format("*"*55, "*"*55))
    pp.pprint(collection.find_one())
    # Getting a certain item
    print("\n{}\n** Finding a specific single item\n{}\n".format("*"*55, "*"*55))
    pp.pprint(collection.find_one({"word": "Capitaland"}))
    # Getting a certain item by object id
    print("\n{}\n** Finding a single item by object id\n{}\n".format("*"*55, "*"*55))
    pp.pprint(collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))
    # Inserting an object
    print("\n{}\n** Inserting an object and displaying it\n{}\n".format("*"*55, "*"*55))
    collection.insert_one({"word": "Vim", "definition": "The best editor"})
    pp.pprint(collection.find_one({"word": "Vim"}))
