# Generated by Django 2.2.12 on 2020-05-27 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_auto_20200527_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='album',
        ),
    ]
