from django.urls import path

from . import views

app_name = 'api_v1'

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll_list'),
    path('<int:pk>/detail/poll', views.PollDetailView.as_view(), name='poll_detail_update'),
    path('answ/create/', views.AnswerChecker.as_view(), name='answer_create'),
    path('result/<int:pk>/', views.Result.as_view(), name='result')
]