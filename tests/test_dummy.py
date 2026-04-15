import unittest
import os as os
# from mymodule import *

scriptDir=os.path.dirname(__file__)

class Test(unittest.TestCase):
    def test_dummy(self):
        self.assertAlmostEqual(0, 0, places=5)

if __name__ == '__main__':
    unittest.main()
