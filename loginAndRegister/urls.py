from . import views
from django.urls import path,include
urlpatterns =[
    path('login/',views.login_view,name = 'login'),
    path('register/',views.registration_view,name = 'register'),
    path('home/',views.home_view,name = 'home')
]
