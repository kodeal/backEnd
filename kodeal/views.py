from django.shortcuts import render


# main page
def index(request):
    return render(request, 'home.html')


# login page
def login_main(request):
    return render(request, 'login/login_main.html')
