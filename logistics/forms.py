# forms.py

from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['customer', 'destination', 'shipping_date']
        # You can include more fields from your Shipment model if needed


from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'weight', 'location']




from django import forms
from .models import TrackingDetail

class TrackingDetailForm(forms.ModelForm):
    class Meta:
        model = TrackingDetail
        fields = ['date', 'location', 'status']        