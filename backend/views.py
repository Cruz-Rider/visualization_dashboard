from django.shortcuts import render
from rest_framework import generics
from .models import Insights
from .serializers import InsightSerializer

class InsightListAPIView(generics.ListAPIView):
    queryset = Insights.objects.all()
    serializer_class = InsightSerializer