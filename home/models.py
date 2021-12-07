from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class Contact(models.Model):

    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        
         return self.name + "  with email  " + self.email



# Create your models here.
class Notices(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14,blank=True)
    # slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    # views= models.IntegerField(default=0)