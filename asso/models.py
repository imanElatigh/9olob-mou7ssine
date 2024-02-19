from django.db import models
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AssociationUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class AssociationUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(blank=True,null=True)
    nom = models.CharField(max_length=255,blank=True,null=True)
    information = models.TextField(blank=True,null=True)
    adresse = models.CharField(max_length=255,blank=True,null=True)
    tel = models.CharField(max_length=20,blank=True,null=True)
    numeroLicence = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    is_staff = models.BooleanField(default=False,blank=True,null=True)

    objects = AssociationUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'adresse', 'tel','numeroLicence']

    def __str__(self):
        return self.email
class UserAssiocitionProfile(models.Model):
    user_association = models.OneToOneField(AssociationUser,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.user)

class License(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    license_number = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.license_number}"
