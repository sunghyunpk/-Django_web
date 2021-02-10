from django.urls import path

from freeapp.views import FreeListView

app_name = 'freeapp'

urlpatterns = [
    path('list/', FreeListView.as_view(), name='list'),
]