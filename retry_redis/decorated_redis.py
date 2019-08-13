"""
:author: Gatsby Lee
:since: 2019-05-29
"""
import logging

import redis

from retry_redis.retry_decorator import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

LOGGER = logging.getLogger(__name__)

RETRY_EXCEPTIONS = (
    redis.exceptions.ConnectionError,
    redis.exceptions.ResponseError,
    redis.exceptions.TimeoutError,
)

RETRY_DECORATOR = retry(
    retry=retry_if_exception_type(RETRY_EXCEPTIONS),
    wait=wait_exponential(multiplier=1),
    stop=stop_after_attempt(3),
    before_sleep=before_sleep_log(LOGGER, logging.DEBUG),
    reraise=True
)


class Redis(object):

    def __init__(self, **kwargs):
        """
        In order to match keyword arguments to redis-py one,
        custom arguments must not be added.
        """
        self._redis = redis.Redis(**kwargs)
        self._retry_decorator = RETRY_DECORATOR

    def __repr__(self):
        return "%s<%s>" % (type(self).__name__, repr(self._redis))

    def __getattr__(self, key):
        """
        Override to bind function call to redis-py
        """
        redis_method = getattr(self._redis, key)
        return self._retry_decorator(redis_method)


__all__ = (
    'Redis',
)
