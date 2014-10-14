"""
handlers.heartbeat

A callback-based heartbeat handler

"""
import logging

from tornado.web import RequestHandler

version_info = (0, 1, 0)
__version__ = '.'.join(str(v) for v in version_info)

LOGGER = logging.getLogger(__name__)

callbacks = []


class HeartbeatHandler(RequestHandler):
    """Heartbeat handler to determine if a service is healthy."""

    def get(self):
        """Respond with the health of our service."""
        if not all(callback() for callback in callbacks):
            self.set_status(500)
            self.write()

        self.set_status(204)

    def _log(self):
        """Override Tornado to not log 204's from heartbeat."""
        if self.get_status() != 204:
            super(HeartbeatHandler, self)._log()


def register_callback(callable_):
    """Register a callable to be checked during heartbeat.

    This function adds a new heartbeat callback, which can be any
    callable that returns ``True`` if healthy, and ``False`` if
    it detects a problem. Any ``False`` return value will cause
    a call to the ``HeartbeatHandler`` to return a ``500``.

    """
    callbacks.append(callable_)
    LOGGER.info('Callback %s registered', callable_.__name__)
