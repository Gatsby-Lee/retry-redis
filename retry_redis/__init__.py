"""
:author: Gatsby Lee
:since: 2019-05-29
"""
from retry_redis.__about__ import __version__
from retry_redis.decorated_redis import (
    Redis,
)


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


VERSION = tuple(map(int_or_str, __version__.split('.')))


__all__ = (
    '__version__',
    'VERSION',
    'Redis',
)
