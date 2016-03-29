''' API classes for trades '''
import urllib.request as r
import urllib.parse as parse
import json


class SFTrader(object):
    '''
        Encapsulates the endpoints for Stockfighter's
        orderbook and trading API

        Endpoints: https://starfighter.readme.io/docs/heartbeat
    '''

    def __init__(self, account=None, ven=None, stock=None):
        ''' Get Authorizaion information and initialize '''
        if account is None or ven is None or stock is None:
            raise ValueError('Enter values for account, venue and stock')
        self.account = account
        self._venue = ven
        self.stock = stock
        self.url = 'https://api.stockfighter.io/ob/api'
        self.target = (self.url +
                       '/venues' +
                       self._venue +
                       '/stocks' +
                       self.stock +
                       '/orders')

    @property
    def heartbeat(self):
        ''' get api status '''
        resp = json.loads(
            r.urlopen(self.url + '/heartbeat').read().decode('utf8')
        )
        print(resp)
        return 'ok' if resp['ok'] else 'error'

    @property
    def venue(self):
        ''' get venue status '''
        resp = json.loads(
            r.urlopen(
                self.url + '/venues' + self._venue + '/heartbeat'
            ).read().decode('utf8')
        )
        return 'ok' if resp['ok'] else 'error'

    def order(self, price, qty, direction, orderType='limit'):
        ''' Send POST to api url
            Parameters
            **********
            Desired price (an integer: $53.42 becomes 5342). Ignored for market orders.
            price:	     integer (strip decimal and $ sign if present)
            qty:	     integer (Desired quantity)
            dir:	     string (Direction: 'buy' or 'sell')
            orderType:	 string

            Order Types
            ***********
            market:         current market price
            limit:          limit price to specified amount
            fill-or-kill:   meet qty requirement in one go and close or cancel order
            immediate-or-kill: get what you can if fok doesn't work then close
        '''
        data = parse.urlencode([
            ('price', price), ('qty', qty),
            ('direction', direction), ('orderType', orderType)
        ]).encode('utf8')
        print(data)
        #  resp = r.urlopen(self.target, data=data)


if __name__ == '__main__':
    t = SFTrader(account='FEB78069832', ven='BMYBEX', stock='HCC')
    t.order(80.00, 45, 'buy')
    print(t.heartbeat)
