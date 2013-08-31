from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'assistant.views.home'),
    url(r'^test/add$', 'assistant.views.test_add'),
    url(r'^test/detail/(\d+)$', 'assistant.views.test_detail'),
    url(r'^test/filter$', 'assistant.views.test_filter'),
)
