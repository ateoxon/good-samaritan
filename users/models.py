from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on delete: when user is deleted, delete profile / when profile is deleted, do not delete user

    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics'
    )
    vendor = models.BooleanField(default=False)

    phone_Number = models.CharField(blank=True, max_length=124)

    address = models.CharField(
        blank=True,
        max_length=1024,
    )
    city = models.CharField(
        blank=True,
        max_length=1024,
    )

    zip_Code = models.CharField(
        blank=True,
        max_length=12,
    )

    hours = models.CharField(
        blank=True,
        help_text="Hours of Operation",
        max_length=100,
    )

    contact = models.CharField(
        blank=True,
        help_text="Point of Contact",
        max_length=100,
    )

    verified = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
