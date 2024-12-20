from django.urls import path
from .views import registration_view, login_view, logout_view, profile_view, profile_edit, change_password_view


urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('change-password/', change_password_view, name='change_password')

]