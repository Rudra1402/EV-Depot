# Generated by Django 5.0.6 on 2024-07-23 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_cars_user_alter_cars_createdat_alter_cars_image'),
        ('users', '0009_buyer_lastname_buyer_points_buyer_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='purchasedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_cars', to='users.buyer'),
        ),
    ]
