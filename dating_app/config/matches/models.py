from django.db import models

from profiles.models import UserProfile


class Match(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='matches_as_user1')
    user2= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='matches_as_user2')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user1', 'user2'] 


    def __init__(self):
        return f"match between {self.user1.user.username} and {self.user2.user.username}"
        


class Block(models.Model):
    blocker = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blocked_user')
    blocked = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blocked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['blocker', 'blocked']