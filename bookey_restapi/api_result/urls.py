from django.urls import path
from . import views


app_name = 'api_result'
urlpatterns = [
    path('', views.ResultView.as_view()),  # Result에 관한 API를 처리하는 view로 Request를 넘김
]