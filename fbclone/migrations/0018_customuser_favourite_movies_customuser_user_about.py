# Generated by Django 4.2 on 2023-04-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbclone', '0017_messages_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favourite_movies',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]