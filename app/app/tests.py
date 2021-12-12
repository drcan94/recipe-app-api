from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):
    """docstring for."""

    def test_add_numbers(self):
        """ test that two numbers are added together """

        self.assertEqual(add(3, 8), 11)

    def test_substract_nunbers(self):
        """ test that values are substracted and returned """

        self.assertEqual(substract(5, 1), 4)
