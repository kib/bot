from yardbird.irc import IRCResponse
from viewer.models import Image, Link
from bot.utils import parse_request

def hoi(request):
    d = request.reply_recipient
    return IRCResponse(d, 'haai')
