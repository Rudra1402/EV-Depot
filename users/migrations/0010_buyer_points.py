# Generated by Django 5.0.6 on 2024-07-22 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_buyer_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]