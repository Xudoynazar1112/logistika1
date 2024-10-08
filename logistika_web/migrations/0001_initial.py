# Generated by Django 5.1 on 2024-08-17 06:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField()),
                ('sender_address', models.TextField(blank=True, null=True)),
                ('data_load', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('destination', models.TextField(blank=True, null=True)),
                ('cargo_type', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('marking', models.CharField(blank=True, max_length=255, null=True)),
                ('country_origin', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('volume', models.CharField(blank=True, max_length=255, null=True)),
                ('number_seats', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('transport_type', models.CharField(blank=True, choices=[('морской', 'Морской'), ('воздушный', 'Воздушный'), ('наземный', 'Наземный'), ('экспресс', 'Экспресс'), ('группирование', 'Группирование'), ('насыпной груз', 'Насыпной груз')], default='морской', max_length=30, null=True)),
                ('product_insurance', models.TextField(blank=True, null=True)),
                ('special_notes', models.TextField(blank=True, null=True)),
                ('tg_nickname', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
