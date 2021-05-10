from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    #r means regular ^$ meand stop. it is same as writing url('', views.home)  
    path('', views.home),
    #url('login/', login, {'template_name': 'accounts/login.html'})
    path('login/', 
        LoginView.as_view(
            template_name='accounts/login.html'
        ), 
        name="login"
    ),
]