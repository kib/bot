from django.http import HttpResponse
from django.template import Context, loader
from viewer.utils import context
from viewer.models import Image

def index(request):
    template = loader.get_template('viewer/index.html')
    c = context(request)
    return HttpResponse(template.render(c))

def images(request):
    template = loader.get_template('viewer/images.html')
    images = Image.objects.order_by('-posted_time')
    c = context(request)
    c.update({'images': images})
    return HttpResponse(template.render(c))

def youtube(request):
    template = loader.get_template('viewer/index.html')
    c = context(request)
    return HttpResponse(template.render(c))

def image(request):
    '''Returns redirect to a single image'''