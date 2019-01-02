# Generated by Django 2.1.4 on 2019-01-02 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20190102_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('is_vendor', models.BooleanField(default=False, verbose_name='Vendor?')),
                ('phone_Number', models.CharField(blank=True, max_length=124)),
                ('address', models.CharField(default='Address line 1', max_length=1024)),
                ('city', models.CharField(default='City', max_length=1024)),
                ('zip_Code', models.CharField(default='ZIP / Postal code', max_length=12)),
                ('hours', models.CharField(default='Hours', max_length=100)),
                ('contact', models.CharField(default='Point of Contact', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='consumerprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='ConsumerProfile',
        ),
        migrations.DeleteModel(
            name='VendorProfile',
        ),
    ]
