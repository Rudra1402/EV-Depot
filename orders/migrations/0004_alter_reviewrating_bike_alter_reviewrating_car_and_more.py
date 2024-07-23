# Generated by Django 5.0.6 on 2024-07-23 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0009_rating_delete_reviewrating'),
        ('cars', '0003_cars_user_alter_cars_createdat_alter_cars_image'),
        ('orders', '0003_alter_reviewrating_bike_alter_reviewrating_car_and_more'),
        ('trucks', '0002_alter_trucks_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='bike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_ratings', to='bikes.bikes'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_ratings', to='cars.cars'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_ratings', to='trucks.trucks'),
        ),
    ]
