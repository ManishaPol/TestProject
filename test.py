#!/usr/bin/env python\

import unittest
from PyhonTestProject import firstElement


class TestMyFunction(unittest.TestCase):
    def test_first_element(self):
        self.assertEqual(firstElement([1,2,3,4]), 1)
                         
if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

