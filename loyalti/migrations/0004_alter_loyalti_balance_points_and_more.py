# Generated by Django 4.1.2 on 2023-06-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalti', '0003_rename_proints_upgrade_loyaltientity_points_upgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyalti',
            name='balance_points',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loyalti',
            name='total_earned_points',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='loyaltitransaction',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
