from rest_framework import routers
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/', views.IndexView.as_view()),
]

router = routers.DefaultRouter()
