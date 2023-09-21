from django.urls import path
from .views import OrdersByAgent

urlpatterns = [
    path("",OrdersByAgent.as_view(),name="comenzi_agenti")
]