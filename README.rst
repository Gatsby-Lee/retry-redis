.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://badge.fury.io/py/retry-redis.svg
    :target: https://pypi.org/project/retry-redis/

.. image:: https://img.shields.io/travis/Gatsby-Lee/retry-redis.svg
   :target: https://travis-ci.org/Gatsby-Lee/retry-redis


retry-redis
===========

Redis Clieht with customizable retrying capability.


Why did I build this?
---------------------

There are Redis exceptions like below that can be handled by simply retrying it.

This package is built in order to help people who need to solve same problem.

* redis.exceptions.ConnectionError
* redis.exceptions.ResponseError
* redis.exceptions.TimeoutError


Who should use?
---------------

Anybody who wants to have retry logic with Redis.



How to Install
--------------

.. code-block:: bash

    pip install retry-redis


How To Use
----------

Simply import retry decorated Redis and Use it.


.. code-block:: python

    import logging
    from retry_redis import Redis

    logging.basicConfig(level=logging.DEBUG)

    r = Redis(port=6666)
    r.lpush('list:test', 1)

    # This log will be printed.
    # DEBUG:retry_redis.decorated_redis:Finished call to 'redis.client.Redis.lpush' after 0.002(s), this was the 1st time calling it.
    # DEBUG:retry_redis.decorated_redis:Finished call to 'redis.client.Redis.lpush' after 2.005(s), this was the 2nd time calling it.
    # DEBUG:retry_redis.decorated_redis:Finished call to 'redis.client.Redis.lpush' after 6.009(s), this was the 3rd time calling it.


Package Dependency
------------------

* redis
* tenacity

