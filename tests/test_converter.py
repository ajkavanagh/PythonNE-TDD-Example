from __future__ import absolute_import

import unittest

from cf_converter import c_to_f

class Test_CF_Converter(unittest.TestCase):

    # Write a test that fails!
    def test_boiling_point(self):
        self.assertEqual(c_to_f(100), 212)
