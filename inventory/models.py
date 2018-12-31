from django.db import models


# Create your models here.

class Donation(models.Model):

    description = models.CharField(max_length=200, blank=False, default='Describe the Item Here')

    choices = ( #for status
        ('AVAILABLE', 'Item ready to be picked up'),
        ('RESERVED', 'Item reserved by another user'),
        ('RESTOCKING', 'Item may be stocked soon')
    )

    expiry = models.CharField(max_length=200, blank=False, default='Enter expiration date')
    status = models.CharField(max_length=10, choices=choices, default='AVAILABLE')
    misc = models.CharField(max_length=50, default="Misc info about donation")
    donator = models.CharField(max_length=50, blank = True, default = "Enter your username")


    class Meta:
        abstract = True

    def __str__(self):
        return '{0}'.format(self.description)



class Foods(Donation):
    pass

class Drinks(Donation):
    pass

class MiscObjects(Donation):
    pass
