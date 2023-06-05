import unittest
from server import PenManager

class TestHandler(unittest.TestCase):
    def setUp(self):
        PenManager.pens = ['Applepen', 'Lemonpen']

    def test_get_request(self):
        pens = PenManager.get_all_pens()

        self.assertEqual(pens, ['Applepen', 'Lemonpen'])

    def test_post_(self):
        pen_type = 'Pineapple'

        pen_count_before = len(PenManager.pens)
        server.MessageService.add_pen(pen_type)
        pen_count_after = len(PenManager.pens)

        self.assertEqual(pen_count_after, pen_count_before + 1)
        self.assertEqual(PenManager.pens[-1], pen_type + 'pen')


if __name__ == '__main__':
    unittest.main()