from importlib.resources import path
from django.urls import path
from .views import helloworldappview

urlpatterns = [
    path('helloworldapp/', helloworldappview)
]