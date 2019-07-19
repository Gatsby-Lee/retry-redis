retry-redis
===========

.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://img.shields.io/badge/Version-1.1.1-green.svg?style=flat
   :target: https://pypi.org/project/retry-redis/


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

    >>> from retry_redis import Redis
    >>> r = Redis()
    >>> r.lpush('test', 1)


Package Dependency
------------------

* redis
* tenacity

