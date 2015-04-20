from django.db import models

# Create your models here.


class RSSCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    publisher = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class RSSSourceList(models.Model):
    category = models.ForeignKey(RSSCategory)
    url = models.URLField(unique=True)
    add_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_created=True)
    last_hash = models.CharField(default="", max_length=255)