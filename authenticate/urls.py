from django.urls import path
from .views import registerView, logIn, logOut, updateProfile
urlpatterns = [
    path('', registerView, name='register'),
    path('sign-up/', registerView, name='register'),
    path('sign-in/', logIn, name='login'),
    path('logout/', logOut, name="logout"),
    path('profile/', updateProfile, name='profile')
]
