from yardbird.irc import IRCResponse
from bot.utils import *
import requests


def bitcoin(request):
    (c, n, m) = parse_request(request)

    r = requests.get('http://data.mtgox.com/api/1/BTCUSD/ticker', timeout=2)
    if not r.status_code == 200:
        return IRCResponse(c, 'Error fetching current bitcoin value from mtgox')

    decoded = r.json()['return']
    last = decoded['last']['display']
    high = decoded['high']['display']
    low = decoded['low']['display']
    w_avg = decoded['avg']['display']
    vol = decoded['vol']['display']

    response = u'[ last: {} - high: {} - low: {} - w_avg: {} - volume: {} ]'.format(last, high, low, w_avg, vol)

    return IRCResponse(c, response)