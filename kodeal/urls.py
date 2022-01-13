from django.urls import path

from . import views

app_name = 'kodeal'

urlpatterns = [
    # main page
    path('', views.index, name='index'),

    # common page
    path('common/', views.login_main, name='login_main'),   # 로그인 페이지
]