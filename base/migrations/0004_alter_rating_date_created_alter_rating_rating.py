# Generated by Django 5.0.6 on 2024-06-30 22:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_rating_date_created_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
