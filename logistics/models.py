from django.db import models

# Create your models here.
# models.py


class Shipment(models.Model):
    customer = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    shipping_date = models.DateField()

    # Add more fields as needed

    def __str__(self):
        return f"Shipment ID: {self.pk}, Customer: {self.customer}, Destination: {self.destination}, Shipping Date: {self.shipping_date}"


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    weight = models.FloatField()
    location = models.CharField(max_length=50)



class TrackingDetail(models.Model):
    date=models.DateField()
    location=models.CharField( max_length=50)
    status=models.CharField( max_length=100)

