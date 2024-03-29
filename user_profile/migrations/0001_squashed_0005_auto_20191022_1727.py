# Generated by Django 2.2.6 on 2019-10-23 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('user_profile', '0001_initial'), ('user_profile', '0002_auto_20191022_1214'), ('user_profile', '0003_auto_20191022_1219'), ('user_profile', '0004_auto_20191022_1705'), ('user_profile', '0005_auto_20191022_1727')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinc_number', models.CharField(blank=True, max_length=20, verbose_name='CNIC Number')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Permanent Address')),
                ('contact_number', models.CharField(blank=True, max_length=30, verbose_name='Contact Number')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Your Location (City)')),
                ('country', models.CharField(blank=True, max_length=30, verbose_name='Your Nationality (Country)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='About (Bio)')),
                ('occupation', models.CharField(blank=True, max_length=500, verbose_name='Your Occupation')),
            ],
        ),
    ]
