
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=255)
    city = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.IntegerField(primary_key= True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User , null=True , on_delete= models.CASCADE, related_name= "post")

    def __str__(self):
        return self.title
        