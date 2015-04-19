from django.db import models

# Create your models here.


class RSSCategory(models.Model):
    name = models.CharField(max_length=255)



class RSSSourceList(models.Model):
    category = models.ForeignKey(RSSCategory)
    url = models.URLField()
    add_date = models.DateTimeField(auto_now_add=True)