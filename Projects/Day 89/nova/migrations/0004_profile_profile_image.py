# Generated by Django 4.2.4 on 2023-09-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0003_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
