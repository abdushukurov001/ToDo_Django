from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class UserModel(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, default='user/userPhoto.jpg')


class Meta:
    db_table = 'user'
    


