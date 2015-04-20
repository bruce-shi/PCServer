from django.db import models
from django.contrib.auth.models import User
from PCCore.models import KeyWords
from RSSCrawler.models import RSSSourceList
# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    UUID = models.CharField(max_length=255)
    token = models.CharField(max_length=100, default="")
    last_login = models.CharField(max_length=255)


class CacheNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.URLField()
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    keywords = models.ManyToManyField(KeyWords)
    ranks = models.IntegerField(default=0)
    static_url = models.URLField(unique=True)
    parent_list = models.ForeignKey(RSSSourceList)


class UserNewsMap(models.Model):
    user = models.ForeignKey(User)
    news = models.ForeignKey(CacheNews)
    if_send = models.IntegerField(default=0)
    if_viewed = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)


class UserRecords(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField()
    duration = models.FloatField(default=0)
    view_time = models.DateTimeField(auto_now_add=True)