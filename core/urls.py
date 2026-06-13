from django.contrib import admin
from django.urls import path, include
from monitor import views # Make sure to import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add this line to map the root URL to your dashboard view
    path('', views.dashboard, name='dashboard'), 
    # You can keep or remove the 'dashboard/' path below
    path('dashboard/', views.dashboard, name='dashboard_alt'),
]