import unittest
from event_bus import EventBus

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.event_bus = EventBus()

    def test_publish_subscribe(self):
        user_data = {'name': 'Dmytro'}
        expected_data = {}

        def event_handler(data):
            nonlocal expected_data
            expected_data = data

        self.event_bus.subscribe('user_created', event_handler)

        self.event_bus.publish('user_created', user_data)

        self.assertEqual(expected_data, user_data)

    def test_unsubscribe(self):
        user_data = {'name': 'Dmytro'}
        expected_data = {}

        def event_handler(data):
            nonlocal expected_data
            expected_data = data

        subscribed_id = self.event_bus.subscribe('user_created', event_handler)

        self.event_bus.unsubscribe(subscribed_id)

        self.event_bus.publish('user_created', user_data)

        self.assertEqual(expected_data, {})

    def test_multiple_subscribers(self):
        user_data = {'name': 'Dmytro'}
        expected_data_1 = {}
        expected_data_2 = {}

        def event_handler_1(data):
            nonlocal expected_data_1
            expected_data_1 = data

        def event_handler_2(data):
            nonlocal expected_data_2
            expected_data_2 = data

        self.event_bus.subscribe('user_created', event_handler_1)
        self.event_bus.subscribe('user_created', event_handler_2)

        self.event_bus.publish('user_created', user_data)

        self.assertEqual(expected_data_1, user_data)
        self.assertEqual(expected_data_2, user_data)

if __name__ == '__main__':
    unittest.main()