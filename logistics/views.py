from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Shipment,InventoryItem

# Create your views here.
def home(request):
    return render(request, 'home.html')


def reports(request):
    return render(request, 'reports.html')

def shipments_view(request):
    shipments = []  # Placeholder for shipment data
    
    return render(request, 'shipments.html', {'shipments': shipments})



def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to admin-dashboard upon successful login
            return redirect('admin_dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'adminlogin.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'adminlogin.html')
    

    
    
    
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

def is_customer(user):
    return user.groups.filter(name='customer-home').exists()



def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    else:
        return redirect('admin_dashboard')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def manage_shipments(request):
    return render(request, 'manage_shipment.html')


# views.py

from django.shortcuts import render, redirect
from .forms import ShipmentForm

# def add_shipment(request):
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or display a success message
#             return redirect('shipments')
#     else:
#         form = ShipmentForm()
#     return render(request, 'add_shipment.html', {'form': form})

# from django.shortcuts import render, get_object_or_404
# from . models import Shipment


# def shipment_details(request, shipment_id):
#     # Fetch the shipment object based on the shipment ID
#     shipment = get_object_or_404(Shipment, pk=shipment_id)
    
#     # Pass the shipment object to the template for rendering
#     return render(request, 'shipment_details.html', {'shipment': shipment})


def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or home page
            return redirect('shipments')  # Change 'home' to the name of your home URL pattern
    else:
        form = ShipmentForm()

    return render(request, 'add_shipment.html', {'form': form})

def shipments_view(request):
    # Retrieve all customer profiles from the database
    shipment = Shipment.objects.all()
    return render(request, 'shipments.html', {'shipment': shipment})
from . import forms, models


def delete_shipment_view(request,pk):
    j=models.Shipment.objects.get(id=pk)
    j.delete()
    return redirect('shipments')


from .forms import InventoryItemForm
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or home page
            return redirect('inventory')  # Change 'home' to the name of your home URL pattern
    else:
        form = InventoryItemForm()

    return render(request, 'add_inventory.html', {'form': form})

# views.py
from django.shortcuts import render
from .models import InventoryItem

def inventory(request):
    # Retrieve all inventory items from the database
    invent = InventoryItem.objects.all()
    return render(request, 'inventory.html', {'invent': invent})


from . import forms, models


def delete_inventory_view(request,pk):
    j=models.InventoryItem.objects.get(id=pk)
    j.delete()
    return redirect('inventory')



def track_shipment(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        # Here you can implement logic to retrieve tracking information
        # based on the provided tracking number and pass it to the template
        tracking_info = get_tracking_info(tracking_number)  # Implement this function
        return render(request, 'tracking.html', {'tracking_info': tracking_info})
    else:
        return render(request, 'tracking.html')
    



from django.http import HttpResponse

# views.py

from django.shortcuts import render, redirect
from .forms import TrackingDetailForm

def add_tracking_details(request):
    if request.method == 'POST':
        form = TrackingDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracking_details')  # Redirect to a success URL
    else:
        form = TrackingDetailForm()
    return render(request, 'add_tracking.html', {'form': form})


from .models import TrackingDetail

def tracking_details(request):
    # Retrieve all tracking details from the database
    tracking_details = TrackingDetail.objects.all()
    # Render the HTML template with the tracking details
    return render(request, 'tracking_details.html', {'tracking_details': tracking_details})    



def customer_login(request):
    return render(request, 'customer_login.html')


def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def customer_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_login')  # Redirect to the customer login page
    else:
        form = UserCreationForm()
    return render(request, 'customer_signup.html', {'form': form})




# views.py

from django.shortcuts import render
from django.http import HttpResponse

def contact_us(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # For demonstration purposes, print the form data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Optionally, you can save the form data to a database or send an email
        
        return HttpResponse("Thank you for your message! We'll get back to you soon.")
    else:
        # Render the contact form template
        return render(request, 'contact_us.html')

def about_us(request):
        return render(request, 'about_us.html')

    