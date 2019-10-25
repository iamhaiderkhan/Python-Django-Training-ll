# Generated by Django 2.2.6 on 2019-10-25 06:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('user_profile', '0001_squashed_0005_auto_20191022_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host', models.CharField(max_length=255)),
                ('email_host_user', models.CharField(max_length=255)),
                ('email_host_password', models.CharField(max_length=255)),
                ('email_post', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Email post is not valid. Email post format should be 000 in digits.', regex='[0-9]{3}')])),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.Site')),
            ],
        ),
    ]