#!/usr/bin/env python3
""" insert in school collection"""

def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert_one(kwargs).inserted_id
