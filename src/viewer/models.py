from django.db import models

class BaseLink(models.Model):
    '''Base class for all link like objects'''
    dest_url = models.CharField(max_length=255)
    nsfw = models.BooleanField(default=False)
    posted_time = models.DateTimeField(auto_now=True)
    posted_channel = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Image(BaseLink):
    mirrored = models.BooleanField(default=False)
    content_type = models.CharField(max_length=255)

    def __unicode__(self):
        return '<Image: {0}>'.format(self.dest_url)

class Link(BaseLink):
    def __unicode__(self):
        return '<Link: {0}>'.format(self.dest_url)

class Video(BaseLink):
    _site_choices = (('Y', 'Youtube'), ('V', 'Vimeo'))
    site = models.CharField(max_length=2, choices=_site_choices)
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return '<Video: {0}>'.format(self.title)

class Topic(models.Model):
    '''Keeps topic history'''
    time = models.DateTimeField(auto_now=True)
    channel = models.CharField(max_length=255)
    nick = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
