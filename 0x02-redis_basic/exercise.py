#!/usr/bin/env python3
""" excercise module """
import uuid
from functools import wraps
from typing import Any, Callable, Optional, Union

import redis


def count_calls(call: Callable) -> Callable:
    """count calls"""

    @wraps(call)
    def wrapper(self, *args, **kwargs):
        key = f"{call.__qualname__}"
        self._redis.incr(key)
        return call(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        val = self._redis.get(key)
        if not val:
            return None
        if val and fn is not None:
            return fn(val)
        return val

    def get_str(self, val: str):
        return self.get(val, lambda x: x.decode("utf-8"))

    def get_int(self, val: str):
        return self.get(val, lambda x: int(x))
