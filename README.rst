sprockets.handlers.heartbeat
============================
A callback-based heartbeat handler

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
``sprockets.handlers.heartbeat`` is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.handlers.heartbeat>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.handlers.heartbeat

Documentation
-------------
https://sprocketshandlersheartbeat.readthedocs.org

Requirements
------------
-  `tornado <https://github.com/tornadoweb/tornado>`_

Example
-------
This examples demonstrates how to use ``sprockets.handlers.heartbeat`` by
registering the ``check_database`` method that is invoked each time a request
to ``/heartbeat`` is made.

.. code:: python

    from sprockets.handlers import heartbeat
    from tornado import web


    def check_database():
        """Any check method should return a bool specifying the check is ok.

        :rtype: bool

        """
        return True

    # Register the check method
    heartbeat.register_callback(check_database)

    # Create a Tornado application
    app = web.Application([('/heartbeat', heartbeat.HeartbeatHandler)])

Version History
---------------
Available at https://sprocketshandlersheartbeat.readthedocs.org/en/latest/history.html

.. |Version| image:: https://badge.fury.io/py/sprockets.handlers.heartbeat.svg?
   :target: http://badge.fury.io/py/sprockets.handlers.heartbeat

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.handlers.heartbeat.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.handlers.heartbeat

.. |Coverage| image:: https://img.shields.io/coveralls/sprockets/sprockets.handlers.heartbeat.svg?
   :target: https://coveralls.io/r/sprockets/sprockets.handlers.heartbeat

.. |Downloads| image:: https://pypip.in/d/sprockets.handlers.heartbeat/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.handlers.heartbeat

.. |License| image:: https://pypip.in/license/sprockets.handlers.heartbeat/badge.svg?
   :target: https://sprocketshandlersheartbeat.readthedocs.org
