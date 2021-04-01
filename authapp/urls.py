from django.urls import path, re_path

from authapp.views import login, register, logout, profile, verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]