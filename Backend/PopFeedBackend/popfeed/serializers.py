from rest_framework import serializers
from .models import UserAccount, UserFollowing, PopPosts, PopLikes, PopComments, PopRepop, CommentLikes
from django.contrib.auth import get_user_model, authenticate

# Users

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, clean_data):
            user_obj = UserAccount.objects.create_user(
                email = clean_data['email'],
                password = clean_data['password'])
            user_obj.username = clean_data['username']
            user_obj.save()

# Content

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'handle', 'bio']

class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['follower_id', 'followee_id', 'created_at']

class PopPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopPosts
        fields = ['pop_id', 'user_id', 'created_at', 'content']

class PopLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopLikes
        fields = ['pop_id', 'user_id', 'created_at']

class PopCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopComments
        fields = ['comment_id', 'pop_id', 'user_id', 'content', 'created_at']

class PopRepopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopRepop
        fields = ['pop_id', 'user_id', 'created_at']

class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ['comment_id', 'user_id', 'created_at']
