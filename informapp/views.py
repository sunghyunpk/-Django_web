from django.shortcuts import render

# Create your views here.

def inform_list(request):

    return render(request, 'informapp/list.html')