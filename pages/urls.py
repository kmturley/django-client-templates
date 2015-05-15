from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^angular', views.angular, name='angular'),
    url(r'^plate', views.plate, name='plate'),
    url(r'^$', views.index, name='index'),
]