#!/usr/bin/env python3
""" calculate average score"""

def top_students(mongo_collection):
    """ Top students sorted by average score """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        },
        {
            "$project": {
                "_id": 0,
                "name": "$_id",
                "averageScore": 1
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
