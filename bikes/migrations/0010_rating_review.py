# Generated by Django 5.0.6 on 2024-07-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0009_rating_delete_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(default='Type something'),
        ),
    ]
