from rest_framework import serializers
from .models import *

# Users



# Content

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username','email','password','handle', 'bio']

class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['follower_id', 'followee_id', 'created_at']

class PopPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopPosts
        fields = ['pop_id', 'user_id', 'created_at', 'content', 'reply_to']

class PopLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopLikes
        fields = ['pop_id', 'user_id', 'created_at']


class PopRepopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopRepop
        fields = ['pop_id', 'user_id', 'created_at']
