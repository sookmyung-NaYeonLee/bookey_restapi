from django.urls import path
from . import views

app_name = 'api_book'
urlpatterns = [
    path('', views.BookView.as_view()),  # Book에 관한 API를 처리하는 view로 Request를 넘김
    path('<str:bid>', views.BookView.as_view()),
    path('search/<str:search_key>', views.BookSearchView.as_view())
]
