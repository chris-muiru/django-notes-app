from django.urls import path
from .views import registerView, logIn, logOut, updateProfile
urlpatterns = [
    path('sign-up/', registerView, name='register'),
    path('sign-in/', logIn, name='login'),
    path('logout/', logOut, name="logout"),
    path('profile/<int:pk>/', updateProfile, name='profile')
]
