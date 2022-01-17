from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'common'

urlpatterns = [
    path('', index, name='index'),

    # 회원가입
    path('signup/', signup, name='signup'),
    path('signup2/', signup2, name='signup2'),

    # Django를 이용한 로그인
    path('login_django/', auth_views.LoginView.as_view(template_name='common/login_django.html'), name='login_django'),
    path('logout_django/', auth_views.LogoutView.as_view(), name='logout_django'),

    # 일반 로그인
    path('login/', login_main, name='login_main'),
    path('logout/', logout_main, name='logout_main'),

    # QnA화면
    path('qna_main/', qna_main, name='qna_main'),
    path('qna_answer/', qna_answer, name='qna_answer'),

]