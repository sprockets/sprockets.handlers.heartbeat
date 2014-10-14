Examples
========
The following example demonstrates how to create a method that is invoked on
each call to ``/heartbeat`` in a web application.

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
