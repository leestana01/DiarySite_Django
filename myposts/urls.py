from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post/', views.diary_post, name='diary_post'),
    path('<int:pk>/', views.diary_detail, name='diary_detail'),
]