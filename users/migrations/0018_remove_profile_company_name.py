# Generated by Django 2.1.4 on 2019-01-03 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='company_Name',
        ),
    ]
