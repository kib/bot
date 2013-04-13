from yardbird.irc import IRCResponse
from bot.utils import *
import requests


def bitcoin(request):
    (c, n, m) = parse_request(request)

    r_usd = requests.get('http://data.mtgox.com/api/1/BTCUSD/ticker', timeout=2)
    if not r_usd.status_code == 200:
        return IRCResponse(c, 'Error fetching current bitcoin value from mtgox')
    r_eur = requests.get('http://data.mtgox.com/api/1/BTCEUR/ticker', timeout=2)
    if not r_eur.status_code == 200:
        return IRCResponse(c, 'Error fetching current bitcoin value from mtgox')


    usd_dec = r_usd.json()['return']
    eur_dec = r_eur.json()['return']

    info_dict = {
        'usd_last': usd_dec['last']['display'],
        'usd_high': usd_dec['high']['display'],
        'usd_low': usd_dec['low']['display'],
        'usd_vol': usd_dec['vol']['display'],
        'usd_avg': usd_dec['avg']['display'],
        'eur_last': eur_dec['last']['display'],
        'eur_high': eur_dec['high']['display'],
        'eur_low': eur_dec['low']['display'],
        'eur_vol': eur_dec['vol']['display'],
        'eur_avg': eur_dec['avg']['display'],
    }

    response = u'[ MtGox: {usd_last} / {eur_last} | H: {usd_high} / {eur_high} | L: {usd_low} / {eur_low} | V-USD: {usd_vol} V-EUR: {eur_vol} ]'.format(**info_dict)

    return IRCResponse(c, response)