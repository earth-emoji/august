# Generated by Django 2.2.12 on 2020-05-27 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_caption'),
        ('forums', '0004_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='photos.Album'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='accounts.Professional'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forums.Topic'),
        ),
    ]
