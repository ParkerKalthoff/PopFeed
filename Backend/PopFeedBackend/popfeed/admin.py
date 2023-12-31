from django.contrib import admin
from popfeed.models import *

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserFollowing)

admin.site.register(PopPosts)
admin.site.register(PopLikes)
admin.site.register(PopRepop)
admin.site.register(PopBookmark)