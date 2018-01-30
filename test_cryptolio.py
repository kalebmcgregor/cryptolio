import unittest
from cryptolio import roi


class TestRoi(unittest.TestCase):

    def testRoiPositiveValues(self):
        self.assertTrue(roi(1, 1) == 100.0)

    def testRoiNegativeValues(self):
        self.assertTrue(roi(-1, -1) == 100.0)

    def testRoiMixValues(self):
        self.assertTrue(roi(-1, 1) == -100.0)

if __name__ == '__main__':
    unittest.main()


