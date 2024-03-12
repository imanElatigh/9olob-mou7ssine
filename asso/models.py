from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

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
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class AssociationUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=255)
    information = models.TextField()
    adresse = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    numeroLicence = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    bankili_account = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_account = models.CharField(max_length=100, blank=True, null=True)
    facebook_account = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    another_image = models.ImageField(upload_to='another_image/', blank=True, null=True)  # Define another image field


    objects = AssociationUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'adresse', 'tel', 'numeroLicence']

    def __str__(self):
        return self.email



        


class License(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.license_number}"



class Post(models.Model):
    association = models.ForeignKey(AssociationUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models

class Chatbot(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.question




