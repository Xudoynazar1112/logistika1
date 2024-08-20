from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Order(models.Model):
    DELIVER_TYPE = (
        ('морской', 'Морской'),
        ('авиа', 'Авиа'),
        ('железнодорожный', 'Железнодорожный'),
        ('автоперевозки', 'Автоперевозки'),
        ('сборный', 'Сборный'),
        ('мультимодальные', 'Мультимодальные'),
    )

    user = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField()
    sender_address = models.TextField(blank=True, null=True)
    data_load = models.DateField(default=timezone.now, blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    cargo_type = models.CharField(max_length=255, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    marking = models.CharField(max_length=255, blank=True, null=True)
    country_origin = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    number_seats = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    transport_type = models.CharField(max_length=30, choices=DELIVER_TYPE, default='морской', blank=True, null=True)
    product_insurance = models.TextField(blank=True, null=True)
    special_notes = models.TextField(blank=True, null=True)
    tg_nickname = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    interest_rate = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
