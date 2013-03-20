from django.test import TestCase
from bot.utils import *

class UrlFixTest(TestCase):
    def test_without_http(self):
        url='cdn.speld.nl/wp-content/uploads/Wilma-en-Albert.jpg'
        self.assertEqual(fix_url(url), 'http://'+url)

    def test_with_http(self):
        url='http://cdn.speld.nl/wp-content/uploads/Wilma-en-Albert.jpg'
        self.assertEqual(fix_url(url), url)


class VideoUrl(TestCase):
    def test_youtube1(self):
        url = 'http://youtu.be/NLqAF9hrVbY'
        id = ('Y', 'NLqAF9hrVbY')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube2(self):
        url = 'http://www.youtube.com/embed/NLqAF9hrVbY'
        id = ('Y', 'NLqAF9hrVbY')
        self.assertEqual(parse_video_url(url), id)
   
    def test_youtube3(self):
        url = 'https://www.youtube.com/embed/NLqAF9hrVbY'
        id = ('Y', 'NLqAF9hrVbY')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube4(self):
        url = 'http://www.youtube.com/v/NLqAF9hrVbY?fs=1&hl=en_US'
        id = ('Y', 'NLqAF9hrVbY')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube5(self):
        url = 'http://www.youtube.com/watch?v=NLqAF9hrVbY'
        id = ('Y', 'NLqAF9hrVbY')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube6(self):
        url = 'http://www.youtube.com/user/Scobleizer#p/u/1/1p3vcRhsYGo'
        id = ('Y', '1p3vcRhsYGo')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube7(self):
        url = 'http://www.youtube.com/sandalsResorts#p/c/54B8C800269D7C1B/2/PPS-8DMrAn4'
        id = ('Y', 'PPS-8DMrAn4')
        self.assertEqual(parse_video_url(url), id)

    def test_youtube9(self):
        url = 'http://www.youtube.com/watch?v=spDj54kf-vY&feature=g-vrec'
        id = ('Y', 'spDj54kf-vY')
        self.assertEqual(parse_video_url(url), id)

