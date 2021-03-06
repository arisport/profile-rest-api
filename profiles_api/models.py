from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,surname,password= None):
        if not email:
            raise ValueError('User must have an email address')

        # email = self.normalize_email Speak with pantelas
        user = self.model(email= email,name = name, surname = surname)
        user.set_password(password)
        print(user)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,surname,password):
        """Create and save new superuser with given details"""
        user = self.create_user(email,name,surname,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','surname',]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name + " " +self.surname

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self) -> str:
        return self.email

