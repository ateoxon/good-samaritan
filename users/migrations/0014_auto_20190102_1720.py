# Generated by Django 2.1.4 on 2019-01-02 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190102_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hours',
            field=models.CharField(blank=True, help_text='Hours of Operation', max_length=100),
        ),
    ]
