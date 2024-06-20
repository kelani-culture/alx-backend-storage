#!/usr/bin//env python3
"""cache request from users"""
import functools
import time
from datetime import timedelta

import redis
import requests

redis_cli = redis.Redis()


def cache_url(method):
    """function cache url"""

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        cached_content = redis_cli.get(args[0])
        if cached_content:
            return cached_content.decode("utf-8")
        content = method(*args, **kwargs)
        redis_cli.setex(args[0], 10, content)
        return content

    return wrapper


def count_req(method):
    """function count request"""

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        key = f"count:{args[0]}"
        redis_cli.incr(key, 1)
        redis_cli.expire(key, 10)
        return method(*args, **kwargs)

    return wrapper


@cache_url
@count_req
def get_page(url: str) -> str:
    """function get page"""
    resp = requests.get(url)
    return resp.text


# print(get_page('http://slowwly.robertomurray.co.uk'))
