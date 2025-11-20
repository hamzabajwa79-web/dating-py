from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    looking_for = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    interests = models.JSONField(default=list)  # Store as list of strings
    height = models.FloatField(blank=True, null=True)  # in cm
    occupation = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    is_premium = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    


class Photo(models.Model):
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='photos')
    image = models.ImageField(upload_to='user_photos/')
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Swipe(models.Model):
    SWIPE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('super_like', 'Super_like'),
    )

    swiper = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='swipes_given')
    swiped_on = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='swipes_received')
    swipe_type = models.CharField(max_length=10,choices=SWIPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


    class Mate:
        unique_together = ['swiper','swiped_on']



