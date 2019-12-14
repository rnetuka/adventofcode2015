import day02.puzzle as day2

from unittest import TestCase


class Day2Test(TestCase):

    def test_1st_result(self):
        expected = 1606483
        result = day2.wrapping_paper_square_feet()
        self.assertEqual(result, expected)

    def test_2nd_result(self):
        expected = 3842356
        result = day2.total_ribbon_length()
        self.assertEqual(result, expected)
