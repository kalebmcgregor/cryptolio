import requests
import json
import yaml

import coin


with open("wallet.yml") as wallet_file:
    doc = yaml.load(wallet_file)
    portfolio_total_usd = 0
    purchase_total_usd = 0
    for x in doc['coins']:
        cur_coin = coin.Coin(x['id'], x['total'], x['purchase_usd'])
        response = requests.get('https://api.coinmarketcap.com/v1/ticker/%s' % cur_coin.id)
        coin_stats = json.loads(response.text)
        coin_usd_total = cur_coin.total * float(coin_stats[0]['price_usd'])
        portfolio_total_usd += coin_usd_total
        purchase_total_usd += cur_coin.purchase_usd
        coin_roi = (1 - cur_coin.purchase_usd / coin_usd_total) * 100
        print("$%.2f %s, %.2f%% roi, %f total" % (coin_usd_total, cur_coin.id, coin_roi, cur_coin.total))
    total_roi = (1 - purchase_total_usd / portfolio_total_usd) * 100
    total_profit = portfolio_total_usd - purchase_total_usd
    print("$%.2f grand total, %.2f%% total roi, $%.2f profit" % (portfolio_total_usd, total_roi, total_profit))
