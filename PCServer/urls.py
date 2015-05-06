from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PCServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^import_rss/', 'RSSCrawler.views.extract_form_opml'),
    url(r'^register/', 'PCWebService.views.user_register'),
    url(r'^login/', 'PCWebService.views.user_login'),
    url(r'^mobile_login/', 'PCWebService.views.mobile_login'),
    url(r'^mobile_test/', 'PCWebService.views.mobile_test_news'),
)
