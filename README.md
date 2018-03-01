# cryptolio
Instead of using an application on my phone or signing into websites I thought it would be easier to access high level stats of my crypto portfolio by using the coinmarketcap api on the command line. 

## Installing
```
# wherever you like putting your projects
git clone git@github.com:kalebmcgregor/cryptolio.git
cd cryptolio
pip3 install -r requirements.txt
```

## Getting Started
You will want to make sure that you have a wallet.yml file in the same directory as the tool. We use a list of coin dictionaries to hold the attributes for each coin.
```
# example wallet.yml
---
coins:
  - id: ethereum
    total: 1
    purchase_usd: 40

  - id: litecoin
    total: 2
    purchase_usd: 25

# run the main.py program in the same directory as wallet.yml
python3 main.py
```

