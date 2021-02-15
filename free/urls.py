from django.urls import path
from .views import FreeListView

app_name = "free"

urlpatterns = [
    path('list/', FreeListView.as_view(), name='list'),
]