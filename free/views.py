from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from free.models import Free

class FreeListView(ListView):
    model = Free
    context_object_name = 'free_list'
    template_name = 'free/list.html'