from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Board

# def board_list(request):
#     all_boards = Board.objects.all().order_by('-id')
#     page = int(request.GET.get('p', 1))
#     pagenator = Paginator(all_boards, 2)
#     boards = pagenator.get_page(page)
#     return render(request, 'board_list.html', {"boards":boards})

# class BoardDetailView(DetailView):
#     model = Board
#     context_object_name = 'target_board'
#     template_name = 'board/detail.html'

# def board_detail(request, pk):
#     board = Board.objects.get(pk=pk)
#     # pk 에 해당하는 글을 가지고 올 수 있게 된다.
#
#     return render(request, 'board_detail.html', {'board': board})
#     # {'board':board} 로 템플릿에 전달해 준다.

def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board,
    }
    return render(request, 'board/detail.html', context)

class BoardListView(ListView):
    model = Board
    context_object_name = 'board_list'
    template_name = 'board/board_list.html'




