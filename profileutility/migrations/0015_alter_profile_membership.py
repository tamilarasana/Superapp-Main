# Generated by Django 4.1.2 on 2023-06-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileutility', '0014_alter_profile_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='membership',
            field=models.CharField(choices=[('Member', 'Member'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], default='Member', max_length=25),
        ),
    ]
