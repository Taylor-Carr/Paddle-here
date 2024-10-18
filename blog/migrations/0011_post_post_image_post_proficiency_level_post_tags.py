# Generated by Django 4.2.11 on 2024-10-17 21:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null='True', verbose_name='image'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='post',
            name='proficiency_level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, choices=[('free parking', 'Free Parking'), ('family_friendly', 'Family Friendly'), ('no_parking', 'No Parking'), ('pet_friendly', 'Pet Friendly'), ('wheelchair_accessible', 'Wheelchair Accessible')], max_length=50),
        ),
    ]
