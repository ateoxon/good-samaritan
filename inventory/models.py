from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import *



# Create your models here.

class Donation(models.Model):

    description = models.CharField(max_length=200, blank=False, help_text='Describe your donation here')

    choices = ( #for status
        ('AVAILABLE', 'Item ready to be picked up'),
        ('RESERVED', 'Item reserved'),
    )

    expiry = models.CharField(max_length=200, blank=False, help_text="Enter expiration date here")
    status = models.CharField(max_length=10, choices=choices, default='AVAILABLE')
    misc = models.CharField(max_length=50, blank=False, help_text='Miscellaneous info about your donation')
    donator = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        abstract = True

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class Foods(Donation):
    pass

class Drinks(Donation):
    pass

class MiscObjects(Donation):
    pass
