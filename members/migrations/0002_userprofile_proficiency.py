# Generated by Django 4.2.11 on 2024-10-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='proficiency',
            field=models.CharField(blank=True, choices=[('begginer', 'Begginer'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20),
        ),
    ]