from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
