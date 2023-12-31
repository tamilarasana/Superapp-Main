# Generated by Django 4.1.2 on 2023-03-13 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showcase', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_type', models.CharField(choices=[('text', 'text'), ('image', 'image')], default='image', max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/images')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('page_navigation', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='NotificationManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('APP_NOTIFICATION', 'APP_NOTIFICATION'), ('PUSH_NOTIFICATION', 'PUSH_NOTIFICATION'), ('SPECIAL_NOTIFICATION', 'SPECIAL_NOTIFICATION'), ('DIRECT_NOTIFICATION', 'DIRECT_NOTIFICATION'), ('SMS_NOTIFICATION', 'SMS_NOTIFICATION'), ('WHATSAPP_NOTIFICATION', 'WHATSAPP_NOTIFICATION'), ('EMAIL_NOTIFICATION', 'EMAIL_NOTIFICATION'), ('OTHER', 'OTHER')], default='APP_NOTIFICATION', max_length=50)),
                ('notification_title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/images')),
                ('description', models.TextField(blank=True, null=True)),
                ('from_date', models.DateTimeField(blank=True, null=True)),
                ('to_date', models.DateTimeField(blank=True, null=True)),
                ('schedule_time', models.TimeField(blank=True, null=True)),
                ('schedule_type', models.CharField(choices=[('HOURLY_NOTIFICATION', 'HOURLY_NOTIFICATION'), ('DAILY_NOTIFICATION', 'DAILY_NOTIFICATION'), ('WEEKLY_NOTIFICATION', 'WEEKLY_NOTIFICATION'), ('MONTHLY_NOTIFICATION', 'MONTHLY_NOTIFICATION'), ('QUATERLY_NOTIFICATION', 'QUATERLY_NOTIFICATION'), ('YEARLY_NOTIFICATION', 'YEARLY_NOTIFICATION'), ('LATER_NOTIFICATION', 'LATER_NOTIFICATION')], default='DAILY_NOTIFICATION', max_length=50)),
                ('recurring', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('PAUSE', 'PAUSE'), ('DISABLE', 'DISABLE')], default='ACTIVE', max_length=50)),
            ],
            options={
                'verbose_name': 'Notification Manager',
                'verbose_name_plural': 'Notification Manager',
                'ordering': ['notification_title'],
            },
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FeaturedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('page_navigation', models.CharField(blank=True, max_length=255, null=True)),
                ('promoted_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promoted_item', to='showcase.itemdescription')),
                ('promotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion', to='promotions.promotions')),
            ],
            options={
                'verbose_name': 'Fetured Item',
                'verbose_name_plural': 'Featured Items',
            },
        ),
    ]
