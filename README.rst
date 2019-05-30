retry-redis
===========

.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://img.shields.io/badge/Version-1.1.0-green.svg?style=flat
   :target: https://pypi.org/project/retry-redis/


Redis Clieht with customizable retrying capability.


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

