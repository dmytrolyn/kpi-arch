import unittest
from unittest import mock

from client import Client

class TestHandler(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_get_request(self, mock_urlopen):
        expected_response = ['Applepen, Pineapplepen']
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value.decode.return_value = '[' + ', '.join('"' + item + '"' for item in expected_response) + ']'
        mock_urlopen.return_value = mock_response

        client = Client()
        pens = client.get_all_pens()

        self.assertEqual(pens, expected_response)
        mock_urlopen.assert_called_once()

    @mock.patch('urllib.request.urlopen')
    def test_post_request(self, mock_urlopen):
        expected_response = 'Pineapplepen'
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_urlopen.return_value = mock_response

        client = Client()
        response = client.add_pen(expected_response)

        self.assertEqual(response, 'Successfully created')
        mock_urlopen.assert_called_once()

if __name__ == '__main__':
    unittest.main()