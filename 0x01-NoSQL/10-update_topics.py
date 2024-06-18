#!/usr/bin/env python3
""" change all topic in school collection"""

def update_topics(mongo_collection, name, topics):
    """ update topics in school"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
