from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'hoi', 'bot.views.hoi', name='hoi'),
    url(r'(?P<url>(https?://|www\.)\S+\.(jpg|png|gif|bmp|jpeg|tiff))', 'bot.views.image', name='image'),
    url(r'(?P<url>(\S*(?P<site>(youtu.be|vimeo.com|youtube.com))/\S+))', 'bot.views.video', name='video'),
    url(r'(?P<url>(https?://|www\.)\S+)', 'bot.views.link', name='link'),
)
