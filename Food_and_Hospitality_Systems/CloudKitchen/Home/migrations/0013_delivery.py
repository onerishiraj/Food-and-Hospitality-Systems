# Generated by Django 3.2.2 on 2021-05-14 04:35

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20210511_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=10)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('vehicle_registration_certificate', models.FileField(blank=True, null=True, upload_to=Home.models.vehicle_registration_certificate_directory_path)),
                ('driving_license', models.FileField(blank=True, null=True, upload_to=Home.models.driving_license_directory_path)),
            ],
        ),
    ]
