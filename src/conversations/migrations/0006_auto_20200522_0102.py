# Generated by Django 2.2.12 on 2020-05-22 01:02

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0005_auto_20200521_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=martor.models.MartorField(),
        ),
    ]