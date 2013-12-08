from yardbird.irc import IRCResponse
from viewer.models import Image, Link
from bot.utils import parse_request
from bs4 import BeautifulSoup
import requests

def civ5(request):
    d = request.reply_recipient
    game_url = 'http://multiplayerrobot.com/Game/Details?id=8343'
    data = requests.post(game_url, headers={'Content-Length': '0'})
    if data.status_code != 200:
        return IRCResponse(d, 'Unable to fetch game data')

    soup = BeautifulSoup(data.text)

    active_player = soup.find(class_='game-host').find(class_='avatar').attrs['title']
    turn_timer = soup.find(id='turn-timer-container').find('strong').string

    return IRCResponse(d, "Active player: {0}, turn ends: {1}".format(active_player, turn_timer))
