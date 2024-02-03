from rest_framework import serializers
from .models import *

# Users # Users # Users # Users # Users # Users # Users # Users 

class UserAccountSerializer_With_Password_And_Email(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username','email','password','handle', 'bio']

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username','handle', 'bio']

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class UserAccountSerializer_No_Bio(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username','handle']

# Content # Content # Content # Content # Content # Content 

class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['follower_id', 'followee_id', 'created_at']

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class PopPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopPosts
        fields = ['pop_id', 'user_id', 'created_at', 'content', 'reply_to']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {"pop": data}

class PopPostsSerializer_No_Title(serializers.ModelSerializer):
    class Meta:
        model = PopPosts
        fields = ['pop_id', 'user_id', 'created_at', 'content', 'reply_to']

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class PopLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopLikes
        fields = ['pop_id', 'user_id', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {"like": data}

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class PopRepopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopRepop
        fields = ['pop_id', 'user_id', 'created_at']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {"repop": data}

### - ### - ### - ### - ### - ### - ### - ### - ### - 

class PopBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopBookmark
        fields = ['pop_id', 'user_id']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {"bookmark": data}
