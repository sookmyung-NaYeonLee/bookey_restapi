from django.urls import path
from . import views

app_name = 'api_book'
urlpatterns = [
    path('', views.BestSellerRankView.as_view()),  # Book에 관한 API를 처리하는 view로 Request를 넘김
    path('<str:bid>', views.BestSellerRankView.as_view()),
]