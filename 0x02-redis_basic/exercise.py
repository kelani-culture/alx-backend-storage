#!/usr/bin/env python3
""" excercise module """
import uuid
from functools import wraps
from typing import Any, Callable, Optional, Union

import redis


def count_calls(method: Callable) -> Callable:
    """count calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """functon wrapper"""
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """call history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """func wrapper"""
        key = f"{method.__qualname__}:inputs"
        self._redis.rpush(key, str(args))
        result = method(self, *args, *kwargs)
        key = f"{method.__qualname__}:outputs"
        self._redis.rpush(key, str(result))
        return result

    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """the function store"""
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """the function get"""
        val = self._redis.get(key)
        if not val:
            return None
        if val and fn is not None:
            return fn(val)
        return val

    def get_str(self, val: str):
        """the functon get string"""
        return self.get(val, lambda x: x.decode("utf-8"))

    def get_int(self, val: str):
        """the function get in"""
        return self.get(val, lambda x: int(x))
