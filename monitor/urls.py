from django.urls import path
from . import views

urlpatterns = [
    # Ithu koduthal 'http://127.0.0.1:8000/' kodukkumpol thanne dashboard open aakum
    path('', views.dashboard, name='dashboard'), 
]