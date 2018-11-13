# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point
from django.contrib.postgres.fields import ArrayField, JSONField


class Company(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(
        max_length=128, null=True, blank=True)
    address = models.CharField(
        max_length=256, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    position = geo_models.PointField(
        null=True, blank=True
    )
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.position = Point(
                self.latitude, self.longitude, srid=4326
            )
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Slot(models.Model):
    company = models.ForeignKey(Company)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    availability = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.time

class BookedSlot(models.Model):
    slot = models.ForeignKey(Slot)
    user = models.ForeignKey(User)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)