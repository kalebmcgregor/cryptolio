import unittest
from cryptolio.coin import Coin


class TestCoin(unittest.TestCase):

    def testCoinInit(self):
        coin = Coin('bitcoin', 1, 1)
        self.assertTrue(coin.total == 1 and coin.id == 'bitcoin' and coin.purchase_usd == 1)

if __name__ == '__main__':
    unittest.main()


