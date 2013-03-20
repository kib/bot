from yardbird.irc import IRCResponse
from viewer.models import Image, Link
from bot.utils import *

def video(request, site=None, url=None):
    print request.__dict__
    print 'site', site
    print 'url', url
    url = fix_url(url)
    parse_video_url(url)
    return IRCResponse('#test', 'got site {0} url {1}'.format(site, url))
    (c, n, m) = parse_request(request)
    nsfw = True if 'nsfw' in m else False
    img_obj = Image.objects.create(dest_url=url, nsfw=nsfw, posted_channel=c, posted_by=n, message=m)
    return IRCResponse()