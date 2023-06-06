import unittest

from layers import PresentationLayer, DataLayer, BusinessLayer

class TestHandler(unittest.TestCase):
    def test_layered_architecture(self):
        data_layer = DataLayer()
        business_logic = BusinessLayer(data_layer)
        presentation = PresentationLayer(business_logic)

        expected_output = [
            "Business data:",
            "First",
            "Second",
            "Third"
        ]

        import sys
        from io import StringIO
        stdout = sys.stdout
        sys.stdout = StringIO()

        presentation.display_data()

        output = sys.stdout.getvalue().strip().split('\n')

        sys.stdout = stdout

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()