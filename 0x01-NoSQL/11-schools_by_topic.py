#!/usr/bin/env python3
""" filter school by topic """

def schools_by_topic(mongo_collection, topic):
    """ school by topic """
    return [topic for topic in mongo_collection.find({"topics": topic})]
