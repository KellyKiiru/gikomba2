# Generated by Django 4.2.4 on 2023-08-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothe_type', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('origin_country', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=1, default=40, max_digits=7)),
                ('age', models.DecimalField(decimal_places=1, default=18, max_digits=7)),
                ('gender', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('pieces', models.DecimalField(decimal_places=1, default=100, max_digits=7)),
                ('price', models.DecimalField(decimal_places=1, default=7999, max_digits=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
