import unittest
from unittest.mock import patch
from main import Peer

class TestPeer(unittest.TestCase):
    def test_add_peer(self):
        peer1 = Peer("Peer 1")
        peer2 = Peer("Peer 2")

        peer1.add_peer(peer2)

        self.assertIn(peer2, peer1.peers)
        self.assertIn(peer1, peer2.peers)

    def test_send_message(self):
        peer1 = Peer("Peer 1")
        peer2 = Peer("Peer 2")

        peer1.add_peer(peer2)

        with patch.object(peer2, 'receive_message') as mock_receive_message:
            peer1.send_message(peer2, "Hello")

            mock_receive_message.assert_called_once_with(peer1, "Hello")

    def test_receive_message(self):
        peer1 = Peer("Peer 1")
        peer2 = Peer("Peer 2")

        peer1.add_peer(peer2)

        with patch('builtins.print') as mock_print:
            peer2.receive_message(peer1, "Hi there")

            mock_print.assert_called_once_with("Peer 2 received a message from Peer 1: Hi there")

if __name__ == '__main__':
    unittest.main()