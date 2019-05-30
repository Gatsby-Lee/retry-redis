retry-redis
===========

redis-py with retry decoration


How to Install
--------------

.. code-block:: bash

    pip install retry-redis


How To Use
----------

Simply import retry decorated Redis and Use it.

.. code-block:: python

    >>> from retry_redis import Redis
    >>> r = Redis()
    >>> r.lpush('test', 1)
