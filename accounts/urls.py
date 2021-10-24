from django.urls import path
from django.conf.urls import include
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [  
    path('', include('rest_auth.urls')),
    path('register', views.userRegister),
    path('login', views.userLogin),
    path('logout', views.userLogout),
]
