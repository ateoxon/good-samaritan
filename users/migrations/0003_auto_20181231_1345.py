# Generated by Django 2.1.4 on 2018-12-31 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_randomtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='randomText',
            field=models.TextField(blank=True),
        ),
    ]