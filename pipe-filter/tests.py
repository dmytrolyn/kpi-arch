import unittest
from filters import uppercase, hyphen

from main import run_pipe

class TestPipeFilter(unittest.TestCase):
    def test_filter_uppercase(self):
        input_data = 'hello'
        expected_output = 'HELLO'
        result = uppercase(input_data)
        self.assertEqual(result, expected_output)

    def test_filter_hyphen(self):
        input_data = 'Hello'
        expected_output = 'H-e-l-l-o'
        result = hyphen(input_data)
        self.assertEqual(result, expected_output)

    def test_run_pipe(self):
        input_data = 'hello'
        expected_output = 'H-E-L-L-O'
        result = run_pipe(input_data)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()