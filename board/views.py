from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Board

# def board_list(request):
#     all_boards = Board.objects.all().order_by('-id')
#     page = int(request.GET.get('p', 1))
#     pagenator = Paginator(all_boards, 2)
#     boards = pagenator.get_page(page)
#     return render(request, 'board_list.html', {"boards":boards})

class BoardDetailView(DetailView):
    model = Board
    context_object_name = 'target_board'
    template_name = 'board/detail.html'

class BoardListView(ListView):
    model = Board
    context_object_name = 'board_list'
    template_name = 'board/board_list.html'
    paginate_by = 25