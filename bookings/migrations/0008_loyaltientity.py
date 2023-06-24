# Generated by Django 4.1.2 on 2023-05-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_accessory_cust_id_or_reg_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltiEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Payment Request', 'Payment Request'), ('New Car Booking', 'New Car Booking'), ('Used Car Booking', 'Used Car Booking'), ('Service Booking', 'Service Booking'), ('Accessory Booking', 'Accessory Booking'), ('Insurance Booking', 'Insurance Booking')], default='Payment Request', max_length=50)),
                ('points_add_per_100', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('points_add_redeem_100', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('time_of_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Loyalti Clause Entity',
                'verbose_name_plural': 'Loyalti Clause Entity',
            },
        ),
    ]