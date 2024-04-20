from django.contrib import admin
from .models import Shipment,InventoryItem,TrackingDetail
# Register your models here.
admin.site.register(Shipment)
admin.site.register(InventoryItem)
admin.site.register(TrackingDetail)

