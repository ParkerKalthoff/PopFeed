from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAccount(AbstractUser):
    handle = models.CharField(max_length=15, null=True)
    bio = models.TextField(max_length=140, blank=True)

class UserFollowing(models.Model):
    follower_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='followers')
    followee_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='followees')
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("follower_id", "followee_id"),)

class PopPosts(models.Model):
    pop_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=140, null=False)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class PopLikes(models.Model):
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("pop_id", "user_id"),)

class PopRepop(models.Model):
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("pop_id", "user_id"),)

class PopBookmark(models.Model):
    pop_id = models.ForeignKey(PopPosts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Primary Key
    class Meta:
        unique_together = (("pop_id", "user_id"),)