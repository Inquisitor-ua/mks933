from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('lesson_plan/', views.lesson_plan, name="lesson_plan"),
    path('informations/', views.informations, name="informations"),
    path('news/<int:news_pk>', views.news, name="news"),
    path('classes/', views.classes, name="classes"),
    path('classinfos/<int:classinfos_pk>', views.classinfos, name="classinfos"),
    path('account/', views.account, name="account"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.log_out, name="logout"),
    path('add_new/', views.add_new, name="add_new"),
]

