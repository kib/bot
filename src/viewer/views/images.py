from django.http import HttpResponse
from django.template import Context, loader
from viewer.utils import context
from viewer.models import Image


def images(request, channel=None, nsfw=None):
    template = loader.get_template('viewer/images.html')
    images = Image.objects.order_by('-posted_time')
    #TODO: this could get expensive with large amounts of images
    channels = set([x.posted_channel for x in Image.objects.all()])
    c = context(request)
    c.update({'images': images, 'channels': channels})
    return HttpResponse(template.render(c))
