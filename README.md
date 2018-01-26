# cryptolio
Instead of using an application on my phone or signing into websites I thought it would be easier to access high level stats of my crypto portfolio by using the coinmarketcap api on the command line. 

## Getting Started
You will want to make sure that you have a wallet.yml file in the same directory as the tool. We use a coins dictionary to hold the attributes for each coin. 
```
# example wallet.yml
---
coins:
  - id: ethereum
    total: 1
    purchase_total: 40

  - id: litecoin
    total: 2
    purchase_total: 25
```

