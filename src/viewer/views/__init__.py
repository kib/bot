from django.http import HttpResponse
from django.template import Context, loader
from viewer.utils import context
from viewer.models import Image
from images import *

def index(request):
    template = loader.get_template('viewer/index.html')
    c = context(request)
    return HttpResponse(template.render(c))


def youtube(request):
    template = loader.get_template('viewer/index.html')
    c = context(request)
    return HttpResponse(template.render(c))

def image(request):
    '''Returns redirect to a single image'''