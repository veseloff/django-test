# Generated by Django 3.2.9 on 2021-11-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_remove_hotel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='link',
            field=models.URLField(max_length=500),
        ),
    ]
