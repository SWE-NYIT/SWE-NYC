from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^events', views.events, name='events'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^opportunities', views.opportunities, name='opportunities'),
]
