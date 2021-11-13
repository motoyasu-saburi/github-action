from unittest import TestCase

from src.mul import multiple


class TestMul(TestCase):

    def test_mul(self):
        self.assertEqual(multiple(2), 4)

    def test_mul2(self):
        self.assertEqual(multiple(2), 4)
