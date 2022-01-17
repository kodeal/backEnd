from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import os
import openai

#OpenAI API 키, 항상 비워놓고 push하기
#openai.api_key = ''
openai.Engine.list()



# home
def index(request):
    return render(request, 'home.html')

# qna
def qna_answer(request):
    return render(request, 'common/qna_answer.html')

# qna action
def qna_main(request):
    if request.method == 'POST':
        user_code = request.POST['code_area']  #코드영역
        user_text = request.POST['text_area']  #질문영역
        #codex 변환 과정
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=user_text,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\"\"\""],
        )
        return render(request, 'common/qna_answer.html', {'response': response})
    else:
        return render(request, 'common/qna_main.html')



# 회뭔가입을 진행하는 함수
def signup(request):
    if request.method == 'POST':
        # 비밀번호 일치 시
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/')    # 메인 페이지(index)로 이동
        # 비밀번호 불일치 시
        else:
            return render(request, 'common/signup.html')
    else:
        return render(request, 'common/signup.html')


# 회뭔가입을 진행하는 함수2
def signup2(request):
    if request.method == 'POST':
        # 비밀번호 일치 시
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/')    # 메인 페이지(index)로 이동
        # 비밀번호 불일치 시
        else:
            return render(request, 'common/signup.html')
    else:
        # 정상적인 회원가입 확인을 위해 로그인, 로그아웃 기능 추가
        form = UserCreationForm
        return render(request, 'common/signup.html', {'form': form})


# 일반 로그인
def login_main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

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
