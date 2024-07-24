# Generated by Django 5.0.7 on 2024-07-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='cover_letter',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='resume',
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(default='', upload_to='resumes/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
