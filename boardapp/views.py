from django.shortcuts import render

from .models import Board

def board_list(request):
    boardapps = Board.objects.all().order_by('-id')
    return render(request, 'boardapp/list.html', context={"boardapps":boardapps})