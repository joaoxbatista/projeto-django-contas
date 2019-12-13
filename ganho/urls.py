from django.urls import path
from .views import *

urlpatterns = [
    path('total', total, name="ganho.total")
]
