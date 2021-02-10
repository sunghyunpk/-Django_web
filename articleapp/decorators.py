from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from articleapp.models import Article

def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

#관리자 권한 확인
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.level == '1' or request.user.level =='0':
            return function(request, *args, **kwargs)
        messages.info(request, "접근권한이 없습니다")
        return redirect('/users/main/')
    return wrap