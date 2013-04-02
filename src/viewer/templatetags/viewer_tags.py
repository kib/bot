from django import template

register = template.Library()

@register.filter
def nsfw_class(value):
    return "nsfw" if value else ""


@register.filter
def channel_class(value):
    c = value.replace('#', '')
    return "channel_{0}".format(c)