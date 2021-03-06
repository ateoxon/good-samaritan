# Generated by Django 2.1.4 on 2019-01-16 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20190115_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='expiry',
            field=models.DateField(blank=True, help_text='Enter expiration date', null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='expiry',
            field=models.DateField(blank=True, help_text='Enter expiration date', null=True),
        ),
        migrations.AlterField(
            model_name='miscobjects',
            name='expiry',
            field=models.DateField(blank=True, help_text='Enter expiration date', null=True),
        ),
    ]
