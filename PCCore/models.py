from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class KeyWords(models.Model):
    user = models.ManyToManyField(User)
    content = models.CharField(max_length=255)
    count = models.BigIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

class Words(models.Model):
    word = models.CharField(max_length=255)
    count = models.BigIntegerField()