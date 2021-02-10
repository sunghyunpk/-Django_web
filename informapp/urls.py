from django.urls import path
from . import views

app_name = "boardapp"

urlpatterns = [
    path('list', views.inform_list)
]