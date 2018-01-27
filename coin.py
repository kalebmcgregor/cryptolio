import requests
import json


class Coin:
    def __init__(self, coin_id, total, purchase_usd):
        self.id = coin_id
        self.total = float(total)
        self.purchase_usd = float(purchase_usd)
        self.response = requests.get('https://api.coinmarketcap.com/v1/ticker/%s' % self.id)
        self.json = json.loads(self.response.text)
        self.price = float(self.json[0]['price_usd'])
        self.balance = float(self.total) * float(self.price)
        self.gain = (self.price * self.total) - self.purchase_usd
