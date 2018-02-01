import unittest
from cryptolio.main import roi, profit


class TestRoi(unittest.TestCase):

    def testRoiPositiveValues(self):
        self.assertTrue(roi(1, 1) == 100.0)

    def testRoiNegativeValues(self):
        self.assertTrue(roi(-1, -1) == 100.0)

    def testRoiMixValues(self):
        self.assertTrue(roi(-1, 1) == -100.0)

    def testRoiLogic(self):
        self.assertTrue(roi(50, 10) == 500.0)


class TestProfit(unittest.TestCase):

    def testProfitPositiveValues(self):
        self.assertTrue(profit(1, 1) == 0)

    def testProfitNegativeValues(self):
        self.assertTrue(profit(-1, -1) == 0)

    def testProfitMixValues(self):
        self.assertTrue(profit(-1, 1) == -2)

    def testProfitLogic(self):
        self.assertTrue(profit(50, 10) == 40)

if __name__ == '__main__':
    unittest.main()


