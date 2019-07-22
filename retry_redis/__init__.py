"""
:author: Gatsby Lee
:since: 2019-05-29
"""

from retry_redis.decorated_redis import (
    DEFAULT_RETRY_EXCEPTIONS,
    Redis,
)

__all__ = (
    'DEFAULT_RETRY_EXCEPTIONS',
    'Redis',
)
