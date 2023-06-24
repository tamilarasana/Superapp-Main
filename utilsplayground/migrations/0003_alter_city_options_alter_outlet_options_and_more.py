# Generated by Django 4.1.2 on 2023-04-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilsplayground', '0002_city_outlet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Outlet City', 'verbose_name_plural': 'Outlet City'},
        ),
        migrations.AlterModelOptions(
            name='outlet',
            options={'verbose_name': 'Outlet Location', 'verbose_name_plural': 'Outlet Location'},
        ),
        migrations.AlterField(
            model_name='outlet',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='utilsplayground.city'),
        ),
    ]
