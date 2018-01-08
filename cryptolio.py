import requests
import json
import yaml


with open("wallet.yml") as wallet_file:
    doc = yaml.load(wallet_file)
    grand_total = 0
    total_purchase = 0
    for coin in doc['coins']:
        response = requests.get('https://api.coinmarketcap.com/v1/ticker/%s' % coin['id'])
        coin_dict = json.loads(response.text)
        total = coin['total']
        coin_usd_total = total * float(coin_dict[0]['price_usd'])
        grand_total += coin_usd_total
        total_purchase += coin['purchase_total']
        coin_roi = (1 - coin['purchase_total'] / coin_usd_total) * 100
        print("$%.2f %s, %.2f%% roi, %f total" % (coin_usd_total, coin['id'], coin_roi, total))
    total_roi = (1 - total_purchase / grand_total) * 100
    total_profit = grand_total - total_purchase
    print("$%.2f grand total, %.2f%% total roi, $%.2f profit" % (grand_total, total_roi, total_profit))
