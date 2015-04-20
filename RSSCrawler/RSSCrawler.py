__author__ = 'bruce'
# coding=utf-8
import urllib2
import feedparser
from goose import Goose
from goose.text import StopWordsChinese
import gzip
from StringIO import StringIO
import langid
import jieba.analyse as ja
import jieba
from PCWebService.models import CacheNews
from PCCore.models import Words
from django.db.models import F
from models import RSSSourceList
import hashlib

# functon to crawl the news webpage and save the information into database
# @raw_html is th rss file which contain the list of each news
#
def crawler_rss(raw_html):

    d = feedparser.parse(raw_html)

    for entry in d.entries:
        # get the cleaned content and summary of the news web page
        article,keywords,words = get_content(entry.link)
        #save the new to the database
        news = CacheNews(title=entry.title,parent_list=css_url,static_url=entry.link,image=article.top_image.src,content=article.cleaned_text,description=entry.summary)
        news.save()

        # add all words todata base to update the tf-idf

        for w in words:
            word = Words.objects.get_or_create(word = w)
            word.count = F('count') +1
            word.save()

        # associate the new with the keywords , many to many relationship
        for w in keywords:
            word = Words.objects.get_or_create(word = w)
            news.keywords.add(word)

        # @TODO send keywords to SVM





# extract webpage info, keywords, and all the seperated words
def get_content(url):
    raw_html =http_request(url)

    # detect the language of the content,if chinese we apply StopWordsChinese
    lan = language_id(content=raw_html)
    if lan:
        if lan[0] == 'zh':
            g = Goose({'stopwords_class': StopWordsChinese})
        else:
            g = Goose()
    else:
        g = Goose()
    article = g.extract(raw_html=raw_html)
    keywords = ja.extract_tags(sentence=raw_html,allowPOS=['nm','n','x','eng','vn'],withWeight=False)
    words = jieba.cut_for_search(sentence=raw_html)
    return article,keywords,words


def language_id(content):
    langid.set_languages(['en', 'zh'])
    return langid.classify(content)

def http_request(url):

    # add the httpHandler to enable debug
    # httpHandler = urllib2.HTTPHandler(debuglevel=1)
    # httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    # url = "http://sports.sina.com.cn/j/2015-04-18/20177579599.shtml"

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders= [('User-Agent','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36'),]
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)

    # handling the website that just ignore you accept-encoding header!
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        raw_html = f.read()
    else:
        raw_html = response.read()
    return raw_html

# main cron function , will be called by the crontab
def cron_job():
    rsslist = RSSSourceList.objects.first()
    for rss in rsslist:
        raw_html = http_request(rss.url)
        last_hash = rss.last_hash
        new_hash = hashlib.md5(raw_html)
        if(not new_hash  == last_hash):
            rss.last_hash = new_hash
            rss.save()
            crawler_rss(raw_html)