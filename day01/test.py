import unittest
import day01.puzzle as day1

from unittest import TestCase


class Day1Test(TestCase):

    def test_1st_answer(self):
        expected = 280
        result = day1.calculate_floor()
        self.assertEqual(result, expected)

    def test_2nd_answer(self):
        expected = 1797
        result = day1.basement_index()
        self.assertEqual(result, expected)
