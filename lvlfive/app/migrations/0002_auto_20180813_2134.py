# Generated by Django 2.0.5 on 2018-08-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='pro_pic',
            new_name='profile_pic',
        ),
    ]