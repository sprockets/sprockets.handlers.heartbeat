"""
Tests for the sprockets.handlers.heartbeat package

"""
import mock
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application


from sprockets.handlers import heartbeat


class _BaseHeartbeatHandlerTestCase(AsyncHTTPTestCase):

    def setUp(self):
        super(_BaseHeartbeatHandlerTestCase, self).setUp()
        self.callback = mock.Mock(__name__='mock')

        self.configure()
        self.execute()

    def execute(self):
        heartbeat.register_callback(self.callback)
        self.http_client.fetch(self.get_url('/heartbeat'), self.stop)
        self.response = self.wait()

    def tearDown(self):
        heartbeat.callbacks = []

    def get_app(self):
        return Application([('/heartbeat', heartbeat.HeartbeatHandler)])


class TestHealthyHeartbeat(_BaseHeartbeatHandlerTestCase):

    def configure(self):
        self.callback.return_value = True

    def test_healthy_heartbeat(self):
        self.assertEqual(self.response.code, 204)

class TestUnhealthyHeartbeat(_BaseHeartbeatHandlerTestCase):

    def configure(self):
        self.callback.return_value = False

    def test_unhealthy_heartbeat(self):
        self.assertEqual(self.response.code, 500)
