# Generated by Django 2.2.12 on 2020-05-02 09:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200501_0524'),
        ('jobs', '0002_job_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('interest', models.TextField(blank=True)),
                ('match', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], max_length=20)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='accounts.Employer')),
                ('job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobs.Job')),
            ],
            options={
                'verbose_name': 'application',
                'verbose_name_plural': 'applications',
            },
        ),
    ]
