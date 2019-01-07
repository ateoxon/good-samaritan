from django.contrib import admin

# Register your models here, models will not show up in admin page unless registered
#as of now, only users and groups are showing

from .models import Post
admin.site.register(Post) #this should register Posts db and should show


admin.site.site_header = "Good Samaritan"
admin.site.site_title = "Good Samaritan"
admin.site.index_title = "Good Samaritan Site Administration"
