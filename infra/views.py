# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import math
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.core.mail import send_mail, EmailMessage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Company, Slot
from .serializers import CompanySerializer, SlotSerializer


class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        if lat and lng:
            p = Point(
                float(lat),
                float(lng),
                srid=4326
            )
        else:
            return Response(
                {'error': 'Please enter lat long'},
                status=status.HTTP_400_BAD_REQUEST
            )
        distance_in_km = 50
        buffer_width = distance_in_km / 40000. * 360. / math.cos(p.y / 360. * math.pi)
        copmanies = Company.objects.filter(
            position__dwithin=(p, buffer_width)
        ).annotate(
            distance=Distance('position', p)
        ).order_by('distance')
        if copmanies.exists():
            comny_serializer = CompanySerializer(
                copmanies, many=True)
            return Response(comny_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                'No Moving company exists in this area',
                status=status.HTTP_200_OK
            )


class SlotViewset(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    queryset = Slot.objects.all()
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        today = datetime.datetime.now().date()
        company_id = request.GET.get('company_id')
        if company_id:
            self.queryset = self.queryset.filter(
                company_id=company_id,
                date__gte=today
            )
        return super(SlotViewset, self).list(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        company_id = request.GET.get('company_id')
        slot_id = request.GET.get('slot_id')

        if company_id and slot_id:
            data = {id: slot_id, 'availability': False}
            serializer = self.get_serializer(
                slot_id, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            'not valid request',
            status=status.HTTP_400_BAD_REQUEST
        )