"""
:author: Gatsby Lee
:since: 2019-05-29
"""
import logging

import tenacity
import redis

LOGGER = logging.getLogger(__name__)
DEFAULT_RETRY_EXCEPTIONS = (
    redis.exceptions.ConnectionError,
    redis.exceptions.ResponseError,
    redis.exceptions.TimeoutError,
)

LOGGER = logging.getLogger(__name__)


class Redis(object):
    """
    Wrapper of redis-py
    """

    def __init__(self, **kwargs):
        """
        In order to match keyword arguments to redis-py one,
        custom arguments must not be added.
        """
        self._redis = redis.StrictRedis(**kwargs)
        self._retry_decorator = tenacity.retry(
            retry=tenacity.retry_if_exception_type(DEFAULT_RETRY_EXCEPTIONS),
            wait=tenacity.wait_exponential(multiplier=1, min=1, max=10),
            stop=tenacity.stop_after_attempt(3),
            after=tenacity.after_log(LOGGER, logging.INFO)
        )

    def __repr__(self):
        return "%s<%s>" % (type(self).__name__, repr(self._redis))

    def __getattr__(self, key):
        """
        Override to bind function call to redis-py
        """
        redis_method = getattr(self._redis, key)
        return self._retry_decorator(redis_method)


StrictRedis = Redis

__all__ = (
    'Redis',
    'StrictRedis',
)
