from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class FreeListView(ListView):
    model = Free
    context_object_name = 'free_list'
    template_name = 'freeapp/list.html'