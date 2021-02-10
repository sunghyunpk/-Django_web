from django.urls import path

from introduceapp.views import IntroduceListView

app_name = 'introduceapp'

urlpatterns = [
    path('list/', IntroduceListView.as_view(), name='list'),

]