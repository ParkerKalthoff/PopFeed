from django.contrib import admin
from popfeed.models import CommentLikes, PopComments, PopLikes, PopPosts, PopRepop, UserAccount, UserFollowing

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserFollowing)

admin.site.register(PopPosts)
admin.site.register(PopLikes)
admin.site.register(PopComments)
admin.site.register(PopRepop)

admin.site.register(CommentLikes)