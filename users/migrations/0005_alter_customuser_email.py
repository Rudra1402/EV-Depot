# Generated by Django 4.2.14 on 2024-07-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=30),
        ),
    ]