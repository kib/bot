from django.contrib import admin
from viewer.models import *

class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_time'
    list_display = ('dest_url', 'posted_channel', 'posted_time', 'posted_by', 'nsfw')

admin.site.register(Image, ImageAdmin)
admin.site.register(Link)
admin.site.register(Video)
