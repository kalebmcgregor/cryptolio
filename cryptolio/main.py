
import argparse

import yaml

from cryptolio.coin import Coin


def roi(gain, cost):
    return gain/cost * 100


def profit(balance, cost):
    return balance - cost


def main(wallet_file):
    with open(wallet_file) as f:
        doc = yaml.load(f)
        portfolio_balance_usd = 0
        purchase_balance_usd = 0
        for coin_dict in doc['coins']:
            coin = Coin(coin_dict['id'], coin_dict['total'], coin_dict['purchase_usd'])
            portfolio_balance_usd += coin.balance
            purchase_balance_usd += coin.purchase_usd
            print("$%.2f %s, %.2f%% roi, $%.2f profit" % (coin.balance, coin.id,
                                                       roi(coin.profit, coin.purchase_usd), coin.profit))
        total_profit = profit(portfolio_balance_usd, purchase_balance_usd)
        print("$%.2f total, %.2f%% roi, $%.2f profit" % (portfolio_balance_usd,
                                                         roi(total_profit, portfolio_balance_usd), total_profit))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate crypto portfolio current stats.')
    parser.add_argument('--wallet_file', dest='wallet_file', type=str, default='wallet.yml')
    args = parser.parse_args()
    main(args.wallet_file)

