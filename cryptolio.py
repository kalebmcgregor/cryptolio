import yaml

from coin import Coin


def roi(gain, cost):
    return gain/cost * 100


def profit(balance, cost):
    return balance - cost


with open("wallet.yml") as wallet_file:
    doc = yaml.load(wallet_file)
    portfolio_balance_usd = 0
    purchase_balance_usd = 0
    for x in doc['coins']:
        coin = Coin(x['id'], x['total'], x['purchase_usd'])
        portfolio_balance_usd += coin.balance
        purchase_balance_usd += coin.purchase_usd
        print("$%.2f %s, %.2f%% roi, %f total" % (coin.balance, coin.id,
                                                  roi(coin.profit, coin.purchase_usd), coin.total))
    total_profit = profit(portfolio_balance_usd, purchase_balance_usd)
    print("$%.2f in portfolio, %.2f%% roi, $%.2f profit" % (portfolio_balance_usd,
                                                            roi(total_profit, portfolio_balance_usd),
                                                            total_profit))
