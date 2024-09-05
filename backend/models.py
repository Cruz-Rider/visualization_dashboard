from django.db import models

class Insights(models.Model):
   
    json_data = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
