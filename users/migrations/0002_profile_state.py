# Generated by Django 2.1.4 on 2019-01-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
