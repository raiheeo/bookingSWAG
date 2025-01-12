# Generated by Django 5.1.4 on 2025-01-12 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_hotel_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_status',
            field=models.CharField(choices=[('cancelled', 'Cancelled'), ('confirmed', 'Confirmed')], max_length=32),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_hotels', to='hotel_app.city'),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_image', to='hotel_app.hotel'),
        ),
    ]