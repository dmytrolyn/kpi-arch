import unittest
from unittest.mock import patch, MagicMock
from broker import Broker
from services import Service1, Service2


class TestHandler(unittest.TestCase):
    def test_broker_subscribe(self):
        broker = Broker()
        callback1 = lambda: None
        callback2 = lambda: None

        broker.subscribe('event', callback1)
        broker.subscribe('event', callback2)

        self.assertEqual(len(broker.subscribers['event']), 2)
        self.assertIn(callback1, broker.subscribers['event'])
        self.assertIn(callback2, broker.subscribers['event'])

    def test_broker_publish(self):
        broker = Broker()
        callback1 = MagicMock()
        callback2 = MagicMock()

        broker.subscribe('event', callback1)
        broker.subscribe('event', callback2)

        service1 = Service1(broker)
        service2 = Service2(broker)

        broker.publish('event')

        callback1.assert_called_once_with()
        callback2.assert_called_once_with()

    def test_service1_handle_event(self):
        broker = Broker()
        service1 = Service1(broker)
        with patch('builtins.print') as mock_print:
            service1.handle_event('Hello', name='World')
            mock_print.assert_called_with('Service 1 processing:', ('Hello',), {'name': 'World'})

    def test_service2_handle_event(self):
        broker = Broker()
        service2 = Service2(broker)
        with patch('builtins.print') as mock_print:
            service2.handle_event('Hello', name='World')
            mock_print.assert_called_with('Service 2 processing:', ('Hello',), {'name': 'World'})


if __name__ == '__main__':
    unittest.main()