import json
from typing import Any
from django.core.management.base import BaseCommand
from backend.models import Insights

class Command(BaseCommand):
    
    help = 'Load Data from raw JSON file'

    def handle(self, *args: Any, **options: Any):
        with open('backend/jsondata.json', 'r', encoding='utf-8') as rawData:
            data = json.load(rawData)
            Insights.objects.bulk_create([Insights(json_data=item) for item in data])
        
        self.stdout.write(self.style.SUCCESS('Data Loaded Successfully'))