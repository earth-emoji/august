# Generated by Django 2.2.12 on 2020-05-18 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200501_0524'),
        ('classifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('name', models.CharField(blank=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'forum',
                'verbose_name_plural': 'forums',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('description', models.TextField(blank=True)),
                ('moderator', models.ForeignKey(blank=True, on_delete=django.db.models.fields.related.ForeignKey, related_name='topics', to='accounts.Professional')),
                ('tags', models.ManyToManyField(blank=True, related_name='topics', to='classifications.Tag')),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.fields.related.ForeignKey, related_name='posts', to='accounts.Professional')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('content', models.TextField(blank=True)),
                ('is_published', models.BooleanField(blank=True, default=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.Professional')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forums.Comment')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forums.Post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
