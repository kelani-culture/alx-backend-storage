#!/usr/bin/env python3
""" show nginx logs in db"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log = client.logs

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{log.nginx.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        count = log.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = log.nginx.count_documents({"method": "GET", "path": "/status"})

    print(f"{status_count} status check")

    pipeline = [
            {
                "$group": {"_id": "$ip", "count": {"$sum": 1}}
            },
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]
    print("IPS")
    agg = log.nginx.aggregate(pipeline)
    for dct in agg:
        dct = list(dct.values())
        print(f"\t{dct[0]}: {dct[1]}")
