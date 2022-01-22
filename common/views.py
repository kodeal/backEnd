import json

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os

# home
from django.views.decorators.csrf import csrf_exempt

from common.models import UserModel


def index(request):
    return render(request, 'home.html')


# 회원가입을 진행하는 함수
@csrf_exempt
def signup(request):
    # GET 방식 호출일 때
    if request.method == 'GET':
        return render(request, 'common/signup.html')
    # POST 방식 호출일 때
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)  # 이름
        user_id = request.POST.get('user_id', None)  # 아이디
        password1 = request.POST.get('password1', None)  # 비밀번호
        password2 = request.POST.get('password2', None)  # 비밀번호(확인)
        email = request.POST.get('email', None)  # 이메일
        res_data = {}

        if not (user_name and user_id and password1 and password2 and email):
            res_data['error'] = "입력하지 않은 칸이 있습니다."
            # print('입력하지 않은 칸이 있습니다.')
        if password1 != password2:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
            print('비밀번호가 일치하지 않습니다.')
        else:
            user = UserModel(user_name=user_name, user_id=user_id, email=email,
                             # password1=make_password(password1), password2=make_password(password2),
                             password1=password1, password2=password2,  # 암호화 적용 함수를 만든 뒤에는 위의 문장으로 대체
                             )
            user.save()
        return render(request, 'home.html', res_data)


# 회뭔가입을 진행하는 함수2
def signup2(request):
    template_name = 'common/login.html'
    data = request.POST
    if User.objects.filter(user_id=data['id'].exists()):
        context = {
            'result': '이미 존재하는 아이디입니다.'
        }
    else:
        User.objects.create_user(
            user_id=data['user_id'],
            user_name=data['user_name'],
            password=data['password1'],
            email=data['email']
        ).save()
        context = {
            'result': '회원가입 성공'
        }
    return HttpResponse(json.dumps(context), content_type='application/json')


# 일반 로그인
def login_main(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(request, user_id=user_id, password=password)

        if user is None:
            return render(request, 'common/login.html', {'error': 'username 또는 password가 틀렸습니다.'})
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'common/login.html')


# 일반 로그아웃
def logout_main(request):
    auth.logout(request)
    return redirect('/')
