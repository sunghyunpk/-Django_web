from django.urls import path
from . import views
from .views import BoardListView #BoardDetailView

app_name = 'board'

urlpatterns = [
    # path('list/', views.board_list),
    path('list/', BoardListView.as_view(), name='list'),
    # path('detail/<int:pk>', BoardDetailView.as_view(), name='detail'),
    # path('detail/<int:pk>/', views.board_detail),
    path('<int:pk>/', views.board_detail_view, name='detail'),

]

