# Generated by Django 2.1.4 on 2019-01-02 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190102_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_vendor',
        ),
    ]