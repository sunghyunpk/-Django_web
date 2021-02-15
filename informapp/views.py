from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from informapp.models import Inform


class InformListView(ListView):
    model = Inform
    context_object_name = 'inform_list'
    template_name = 'informapp/list.html'
