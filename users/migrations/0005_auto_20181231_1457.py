# Generated by Django 2.1.4 on 2018-12-31 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181231_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address2',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Address line 1', max_length=1024),
        ),
    ]
