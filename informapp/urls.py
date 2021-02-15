from django.urls import path
from .views import InformListView

app_name = "informapp"

urlpatterns = [
    path('list/', InformListView.as_view(), name='list'),
]