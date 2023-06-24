# Generated by Django 4.1.2 on 2023-06-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_usedcarbooking_number_of_owners_usedcarbooking_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appbooking',
            name='gateway_order_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appbooking',
            name='gateway_session_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appbooking',
            name='mode_of_payment',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
