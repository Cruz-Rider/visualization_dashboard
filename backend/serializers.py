from rest_framework import serializers
from .models import Insights

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insights
        fields = '__all__'
        