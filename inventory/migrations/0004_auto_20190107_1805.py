# Generated by Django 2.1.4 on 2019-01-08 00:05

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20190107_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='expiry',
            field=models.DateField(help_text='Enter expiration date', validators=[inventory.models.no_past]),
        ),
        migrations.AlterField(
            model_name='foods',
            name='expiry',
            field=models.DateField(help_text='Enter expiration date', validators=[inventory.models.no_past]),
        ),
        migrations.AlterField(
            model_name='miscobjects',
            name='expiry',
            field=models.DateField(help_text='Enter expiration date', validators=[inventory.models.no_past]),
        ),
    ]
