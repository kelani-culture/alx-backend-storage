#!/usr/bin/env python3
""" excercise module """
import uuid
from typing import Union

import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id
