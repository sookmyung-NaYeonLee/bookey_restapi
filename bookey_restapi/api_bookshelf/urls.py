from django.urls import path
from . import views

app_name = 'api_bookshelf'
urlpatterns = [
    path('', views.BookshelfView.as_view()),  # Bookshelf에 관한 API를 처리하는 view로 Request를 넘김
    path('<str:userId>/<str:bookId>', views.BookshelfView.as_view())
]
