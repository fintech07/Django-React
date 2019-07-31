# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework import generics

from django.shortcuts import render

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


