# Generated by Django 4.2.4 on 2024-01-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bales', '0003_delete_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('bale_origin', models.CharField(max_length=100)),
                ('store_owner', models.CharField(max_length=100)),
                ('bale_weight', models.DecimalField(decimal_places=1, default=40, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=50)),
                ('bale_weight', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wholesaler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholesaler_name', models.CharField(max_length=100)),
                ('country_origin', models.CharField(max_length=100)),
                ('weight_classes', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
