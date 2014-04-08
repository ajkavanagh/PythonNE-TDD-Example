from __future__ import absolute_import

import unittest

from cf_converter import c_to_f


class Test_CF_Converter(unittest.TestCase):

    # Write a test that fails!
    def test_boiling_point(self):
        self.assertEqual(c_to_f(100), 212)

    def test_freezing_point(self):
        self.assertEqual(c_to_f(0), 32)

    def test_some_random_temps(self):
        import random
        def _f(n):
            return (n * 9.0) / 5.0 + 32.0

        for x in range(10):
            cent = random.randint(-40, 100)
            self.assertAlmostEqual(c_to_f(cent), _f(cent), places=2)

    def test_minus_40(self):
        self.assertEqual(c_to_f(-40), -40)
