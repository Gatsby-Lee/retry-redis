"""
:author: Gatsby Lee
:since: 2019-04-10
"""
from unittest import mock

import pytest
import redis

from retry_redis import Redis


def test_import_version():
    """
    Test version info importing
    """
    from retry_redis.__about__ import __version__
    assert __version__


def test_object_creation_with_default_value():
    """
    Test that Redis instance could be created with
    default value argument.
    """
    assert Redis()


def test_simple_positive_op():
    """
    Test that simple operation still works
    """
    res = Redis().lpush('list:test', 1)
    assert res


def test_retry_return_orig_exception_op():
    """
    Test that simple operation still works
    """

    with pytest.raises(redis.exceptions.ConnectionError):
        func_lpush = Redis(port=6666).lpush
        # https://github.com/jd/tenacity/issues/106
        # patch sleep not to sleep when exception raises
        func_lpush.retry.sleep = mock.Mock()
        func_lpush('list:test', 1)
