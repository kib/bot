from urlparse import parse_qs, urlparse
import re

def parse_request(request):
    '''Returns some basic properties of the request'''
    return (request.reply_recipient, request.nick, request.message)

def fix_url(url):
    '''If the url does not start with http:// or https://, prepends http://'''
    return 'http://{0}'.format(url) if not url.startswith('http://') and not url.startswith('https://') else url

def parse_video_url(url):
    '''Returns a tuple containing the site and video_id of the input url'''
    url_obj = urlparse(url)
    if 'youtu.be' in url_obj.netloc or 'youtube.' in url_obj.netloc:
        video_id = parse_youtube_url(url_obj)
        video_choice = 'Y'
    elif 'vimeo.com' in url_obj.netloc:
        video_id = parse_vimeo_url(url_obj)
        video_choice = 'V'
    else:
        return None
    if video_id:
        return (video_choice, video_id)
    else:
        return None

def parse_youtube_url(url_obj):
    qs = parse_qs(url_obj.query)
    path = url_obj.path
    fragment = url_obj.fragment
    print path
    if 'v' in qs.keys():
        # Easy case: url contains ?v=<id>
        return qs['v'][0]

    # Catch /v/<id>, /embed/<id>
    r = re.compile(r'.*/(?P<video_id>[\w-]{11})(/\S+)?$')
    match = r.match(path)
    if match:
        return match.group('video_id')

    # Video id may be in the fragment (after the #)
    match = r.match(fragment)
    if match:
        return match.group('video_id')
    
