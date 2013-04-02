from django.template import Context, RequestContext
from viewer.utils import context
from viewer.models import Image
from endless_pagination.decorators import page_template
from django.shortcuts import render_to_response


@page_template('viewer/images/page.html')
def images(request, channel=None, nsfw=None, template='viewer/images/index.html', extra_context=None):
    images = Image.objects.order_by('-posted_time')
    #TODO: this could get expensive with large amounts of images
    channels = set([x.posted_channel for x in Image.objects.all()])
    c = context(request)
    c.update({'images': images, 'channels': channels})
    if extra_context is not None:
        c.update(extra_context)
    return render_to_response(template, c, context_instance=RequestContext(request))
