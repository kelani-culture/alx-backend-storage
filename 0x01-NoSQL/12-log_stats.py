#!/usr/bin/env python3
""" show nginx logs in db"""
from pymongo import MongoClient


def nginx_log():
    """nginx log"
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log = client.logs
    print(f"{nginx_log.nginx.count_documents({})} logs")
    print("Methods:")
    get = nginx_log.nginx.count_documents({"method":"GET"})
    post = nginx_log.nginx.count_documents({"method":"POST"})
    put = nginx_log.nginx.count_documents({"method":"PUT"})
    delete = nginx_log.nginx.count_documents({"method":"DELETE"})
    patch = nginx_log.nginx.count_documents({"method":"PATCH"})
    method = {"GET": get,'POST': post, 'PUT':  put, 'PATCH': patch, 'DELETE': delete}
    for met in method:
        print(f'\tmethod {met}: {method[met]}')

    get_status_count = nginx_log.nginx.count_documents({'method': "GET", "path": "/status"})
    print(f"{get_status_count} status check")
nginx_log()
