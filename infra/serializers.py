# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import serializers

from .models import Company, Slot, BookedSlot

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = '__all__'