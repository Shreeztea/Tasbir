from django.db import models
from user_app.models import UserModel

# class PhotoModel(models.Model):
class PhotoModel(models.Model):    
    photo = models.ImageField(upload_to='upload_pic')
    caption = models.TextField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE)

