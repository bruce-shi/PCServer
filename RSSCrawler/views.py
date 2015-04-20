import listparser
import os
from PCServer import settings
from models import RSSCategory
from models import  RSSSourceList
from django.utils import timezone
from django.http import JsonResponse
def extract_form_opml(request):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print BASE_DIR
    bbc = listparser.parse(BASE_DIR + "/static/feeds.opml")
    sina = listparser.parse(BASE_DIR + "/static/sina_all_opml.xml")
    for feed in bbc.feeds:
        cat = RSSCategory.objects.filter(name=feed.title).first()
        if not cat:
            cat = RSSCategory(name=feed.title, publisher=bbc.meta.title)
            cat.save()
        if not RSSSourceList.objects.filter(url=feed.url):
            source = RSSSourceList(url=feed.url,category=cat,last_update=timezone.now())
            source.save()
    for feed in sina.feeds:
        cat = RSSCategory.objects.filter(name=feed.title).first()
        if not cat:
            cat = RSSCategory(name=feed.title, publisher=bbc.meta.title)
            cat.save()
        if not RSSSourceList.objects.filter(url=feed.url):
            source = RSSSourceList(url=feed.url,category=cat,last_update=timezone.now())
            source.save()
    return JsonResponse({'status':True})