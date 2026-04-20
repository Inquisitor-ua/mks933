from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('lesson_plan/', views.lesson_plan, name="lesson_plan"),
    path('informations/', views.informations, name="informations"),
    path('news/<int:news_pk>', views.news, name="news"),
]

