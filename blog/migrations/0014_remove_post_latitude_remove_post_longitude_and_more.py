# Generated by Django 4.2.11 on 2024-10-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_latitude_post_longitude_alter_post_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='post',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=150),
        ),
    ]
