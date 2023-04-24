from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_subtract_numbers(self):
        x = 10
        y = 6
        res = calc.subtract_first_minus_second(x, y)
        self.assertEqual(res, 4)
