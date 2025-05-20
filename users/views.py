from django.shortcuts import render
from users.forms import LoginForm
from users.forms import SignupForm

# Create your views here.
def login(request):
    # LoginForm인스턴스 생성 후 template에 전달
    form = LoginForm()
    context = {
        "form" : form,
    }

    return render(request, "users/login.html", context)


def signup(request):
    # SignupForm인스턴스 생성 후 template에 전달
    form = SignupForm()
    context = {
        "form" : form,
    }
    return render(request, "users/signup.html", context)