from django.template import Context, loader

def context(request):
    '''Provides a base context'''
    return Context({'url_name': request.resolver_match.url_name})

