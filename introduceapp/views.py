from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from introduceapp.models import Introduce


class IntroduceListView(ListView):
    model = Introduce
    context_object_name = 'introduce_list'
    template_name = 'introduceapp/list.html'