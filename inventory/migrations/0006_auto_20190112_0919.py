# Generated by Django 2.1.4 on 2019-01-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190107_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='receiver',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='foods',
            name='receiver',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='miscobjects',
            name='receiver',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
