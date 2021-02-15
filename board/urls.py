from django.urls import path
from . import views
from .views import board_list

app_name = 'board'

urlpatterns = [
    path('list/', views.board_list),
]

