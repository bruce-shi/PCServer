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
def crawler_rss():
    d = feedparser.parse('http://www.reddit.com/r/python/.rss')
    for entry in d['entries']:
        print(entry.title + entry.link)


def get_content(url):

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

    lan = language_id(content=raw_html)
    if lan:
        if lan[0] == 'zh':
            g = Goose({'stopwords_class': StopWordsChinese})
        else:
            g = Goose()
    else:
        g = Goose()
    article = g.extract(raw_html=raw_html)
    print article.cleaned_text
    #keyw = ja.textrank(article.cleaned_text,withWeight=True,allowPOS=['ns', 'n', 'vn','eng'])
    keyw = ja.extract_tags(article.cleaned_text, withWeight=True,allowPOS=['ns', 'n', 'vn','eng','x'])
    for (w,v) in keyw:
        print w + " : " + str(v)
    return article


def language_id(content):
    langid.set_languages(['en', 'zh'])
    return langid.classify(content)


get_content("http://sports.sina.com.cn/f1/2015-04-19/00037579759.shtml")