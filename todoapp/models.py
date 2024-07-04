from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False)
    createDate=models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    image=models.ImageField(upload_to='cook_images/',null=True, blank=True)
=======
    image = models.ImageField(upload_to='media',null=True, blank=True)

>>>>>>> bcb8e254b220e7b90773ea989cb37587fee694c7
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["completed"]
    
#image2の方針
from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


