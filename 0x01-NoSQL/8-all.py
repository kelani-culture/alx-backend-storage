#!/usr/bin/env python3
""" print all object in mongo shell"""

def list_all(mongo_collection):
    """ list all object in school collection"""
    return mongo_collection.find() if mongo_collection.find() else []
