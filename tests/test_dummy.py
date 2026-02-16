import unittest
import numpy as np    
import os as os
# from mymodule import *

scriptDir=os.path.dirname(__file__)

class Test(unittest.TestCase):
    def test_dummy(self):
        np.testing.assert_almost_equal(0, 0, 5)

if __name__ == '__main__':
    unittest.main()
