from django.db import models
from stores.models import Store

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=120)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_empty = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)
