"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test calc module, must start with test_"""
    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
