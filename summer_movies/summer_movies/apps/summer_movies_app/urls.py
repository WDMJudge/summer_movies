from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^search$', views.search),
    # url(r'^create_the_overly_massive_database$', views.database),
]