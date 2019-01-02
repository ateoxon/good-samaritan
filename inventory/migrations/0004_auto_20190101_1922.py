# Generated by Django 2.1.4 on 2019-01-02 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20181231_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='donator',
            field=models.CharField(blank=True, default='Enter your username', max_length=50),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='misc',
            field=models.CharField(default='Misc info about donation', max_length=50),
        ),
        migrations.AlterField(
            model_name='foods',
            name='donator',
            field=models.CharField(blank=True, default='Enter your username', max_length=50),
        ),
        migrations.AlterField(
            model_name='foods',
            name='misc',
            field=models.CharField(default='Misc info about donation', max_length=50),
        ),
        migrations.AlterField(
            model_name='miscobjects',
            name='donator',
            field=models.CharField(blank=True, default='Enter your username', max_length=50),
        ),
        migrations.AlterField(
            model_name='miscobjects',
            name='misc',
            field=models.CharField(default='Misc info about donation', max_length=50),
        ),
    ]
