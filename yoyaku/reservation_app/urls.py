from django.urls import path
from .views import yamadafunction,BookList

urlpatterns = [
    path('',  yamadafunction),
    path('booklist/',  BookList.as_view()),
    

]