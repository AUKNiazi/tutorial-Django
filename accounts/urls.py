from django.conf.urls import url
from . import views

urlpatterns = [
    #r means regular ^$ meand stop. it is same as writing url('', views.home)  
    url(r'^$', views.home),

]