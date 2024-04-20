from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/',views.inventory, name='inventory'),
    path('reports/', views.reports, name='reports'),
    path('shipments/', views.shipments_view, name='shipments'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('adminclick',views.adminclick_view),
    path('adminlogin/',LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-shipments/', views.manage_shipments, name='manage_shipments'),
    path('add-shipment/', views.add_shipment, name='add_shipment'),
    path('shipments/', views.shipments_view, name='shipments'),
    path('delete-shipment/<int:pk>/', views.delete_shipment_view, name='delete-shipment'),
    # path('add_inventory/', views.add_inventory_item, name='add_inventory_item'),
    path('inventory/', views.inventory, name='inventory'),
    path('delete_inventory/<int:pk>/', views.delete_inventory_view, name='delete_inventory'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('tracking/', views.track_shipment, name='tracking'),
    path('tracking/details/', views.tracking_details, name='tracking_details'),  
    path('add-tracking-details/', views.add_tracking_details, name='add_tracking_details'),
    path('customer-login/', views.customer_login, name='customer_login'), 
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('signup/', views.customer_signup, name='customer_signup'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/',views.about_us, name='about_us'),
]
    



