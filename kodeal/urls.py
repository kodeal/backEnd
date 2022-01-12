from django.urls import path

from . import views

app_name = 'kodeal'

urlpatterns = [
    # main page
    path('', views.index, name='index'),

    # login page
    path('login/', views.login_main, name='login_main'),   # 로그인 페이지
]