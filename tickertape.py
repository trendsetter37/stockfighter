'''
    Classes will be use to monitor stock order book and fills/executions
'''

import websocket
import json
import sys
import os

url = 'wss://api.stockfighter.io/ob/api/ws/{acc}/venues/{ven}/tickertape/stocks/{sto}'
exc = 'wss://api.stockfighter.io/ob/api/ws/{acc}}/venues/{ven}/executions/stocks/{sto}'

acc = 'BPP18621820'
ven = 'KYUBEX'
sto = 'DLYU'

#  stock orderbook websocket
ws = websocket.create_connection(url.format(acc=acc, ven=ven, sto=sto))
ws_exc = websocket.create_connection(url.format(acc=acc, ven=ven, sto=sto))

try:
    while True:
        stock = ws.recv()
        orders = json.loads(ws_exc.recv())['order']
        '''
        {
              "ok": true,
              "symbol":"FERE",
              "venue":"UYIEX",
              "direction":"buy",
              "originalQty":1,
              "qty":0,
              "price":0,
              "orderType":"market",
              "id":30,
              "account":"TAH97715708",
              "ts":"2015-08-10T16:54:25.803619968Z",
              "fills":[
                {
                  "price":8332,
                  "qty":1,
                  "ts":"2015-08-10T16:54:25.803626698Z"
                }
              ],
              "totalFilled":1,
              "open":false
        },
    '''
        if stock is not '':
            os.system('cls')
            print(fills)
            info = json.loads(stock)['quote']

            if 'bid' not in info:
                info['bid'] = 'None'
                info['bidSize'] = 0
            if 'ask' not in info:
                info['ask'] = 'None'
                info['askSize'] = 0
            '''
            {
              "ok": true,
              "quote": { // the below is the same as returned through the REST quote API
                "symbol": "FAC",
                "venue": "OGEX",
                "bid": 5100, // best price currently bid for the stock
                "ask": 5125, // best price currently offered for the stock
                "bidSize": 392, // aggregate size of all orders at the best bid
                "askSize": 711, // aggregate size of all orders at the best ask
                "bidDepth": 2748, // aggregate size of *all bids*
                "askDepth": 2237, // aggregate size of *all asks*
                "last": 5125, // price of last trade
                "lastSize": 52, // quantity of last trade
                "lastTrade": "2015-07-13T05:38:17.33640392Z", // timestamp of last trade,
                "quoteTime": "2015-07-13T05:38:17.33640392Z" // server ts of quote generation
              }
            }
            '''

            print('{:<9}  :  {}'.format('symbol', info['symbol']))
            print('{:<9}  :  {}'.format('venue', info['venue']))
            print('{:<9}  :  {}'.format('bid', info['bid']))
            print('{:<9}  :  {}'.format('ask', info['ask']))
            print('{:<9}  :  {}'.format('bidSize', info['bidSize']))
            print('{:<9}  :  {}'.format('askSize', info['askSize']))
            print('{:<9}  :  {}'.format('bidDepth', info['bidDepth']))
            print('{:<9}  :  {}'.format('askDepth', info['askDepth']))
            print('{:<9}  :  {}'.format('last', info['last']))
            print('{:<9}  :  {}'.format('lastTrade', info['lastTrade']))
            print('{:<9}  :  {}'.format('quoteTime', info['quoteTime']))


except KeyboardInterrupt:
    ws.close()
    sys.exit()
