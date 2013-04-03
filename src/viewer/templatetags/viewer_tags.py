from django import template

register = template.Library()

@register.filter
def nsfw_class(value):
    return 'nsfw' if value else 'sfw'


@register.filter
def nsfw_warning(value):
    return 'NSFW, click to show/hide' if value else ''


@register.filter
def nsfw_warning_label(value):
    return 'label label-warning' if value else ''