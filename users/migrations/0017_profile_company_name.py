# Generated by Django 2.1.4 on 2019-01-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_profile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_Name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
