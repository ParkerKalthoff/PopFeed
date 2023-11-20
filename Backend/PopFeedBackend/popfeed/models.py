from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAccount(AbstractUser):
    handle = models.CharField(max_length=15, null=False)
    bio = models.TextField(max_length=140, blank=True)

class UserFollowing(models.Model):
    follower_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='followers')
    followee_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='followees')
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("follower_id", "followee_id"),)
        managed = False

class PopPosts(models.Model):
    pop_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=140, null=False)

class PopLikes(models.Model):
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("pop_id", "user_id"),)
        managed = False

class PopComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    content = models.TextField(max_length=140, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
class PopRepop(models.Model):
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("pop_id", "user_id"),)
        managed = False

class CommentLikes(models.Model):
    comment_id = models.ForeignKey(PopComments, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("comment_id", "user_id"),)
        managed = False