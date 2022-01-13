from django.shortcuts import render


# main page
def index(request):
    return render(request, 'home.html')


# common page
def login_main(request):
    return render(request, 'common/login_main.html')
