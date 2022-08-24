from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView # 継承する汎用 View のインポート

def yamadafunction(request):
  return HttpResponse('Hello Yamada!')

class BookList(ListView):
    template_name = 'reservation_app/list.html' # template_name='表示するhtmlファイル'
    model = Book