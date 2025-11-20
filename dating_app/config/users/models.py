from django.db import models 
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):

    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    date_of_birth =  models.DateField(max_length=100,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
    

