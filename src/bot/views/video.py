from yardbird.irc import IRCResponse
from viewer.models import Image, Link, Video
from bot.utils import *
import gdata.youtube
import gdata.youtube.service
import datetime

def video(request, site=None, url=None):
    url = fix_url(url)
    p_url = parse_video_url(url)
    (c, n, m) = parse_request(request)

    if not p_url:
        return IRCResponse(c, 'Could not parse video URL')

    (c, n, m) = parse_request(request)
    (site, v_id) = p_url
    if site is 'Y':
        yt_service = gdata.youtube.service.YouTubeService()
        entry = yt_service.GetYouTubeVideoEntry(video_id=v_id)
        title = entry.media.title.text
        duration = int(entry.media.duration.seconds)
        duration_s = str(datetime.timedelta(seconds=duration))
        view_count = entry.statistics.view_count
    else:
        discard()
    nsfw = True if 'nsfw' in m else False
    video_obj = Video.objects.create(dest_url=url, nsfw=nsfw, posted_channel=c, posted_by=n, message=m, site=site, video_id=v_id, title=title)
    return IRCResponse(c,'Video: {0} [{1}]'.format(title, duration_s))