from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields): #**extra_fields: Pass extra optional user fields
        if not email:
            raise ValidationError("Email:without it nobody knows you here")
        email=self.normalize_email(email)#normalizes email
        user=self.model(email=email,**extra_fields)#creates user but  yet not saved
        user.set_password(password)#hashes password to avoid plain text
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,blank=False,null=False)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=55)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    phone_number = PhoneNumberField(unique=True)
    bio=models.CharField(max_length=255,blank=True,null=True)
    created_at=models.DateTimeField( auto_now_add=True)
    profile_picture=models.ImageField(upload_to='profile_pic/',blank=True,null=True)
    objects=UserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    def __str__(self):
        return self.email
