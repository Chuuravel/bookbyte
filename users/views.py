from django.shortcuts import render, redirect
from users.forms import LoginForm
from users.forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
# 로그인
def login(request):
    # LoginForm인스턴스 생성 후 template에 전달
    form = LoginForm()
    context = {
        "form" : form,
    }
    return render(request, "users/login.html", context)

# 회원가입
def signup(request):
    # 폼 입력값이 있는 경우 저장
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = request.POST.get('username', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)
            # genre_choices =  request.POST.get('genre_choices', None)

            # 비밀번호와 비밀번호확인 일치 여부 확인
            if password1 != password2:
                return render(request, "users/signup.html")
            else:
                user = User()
                user.username = username
                user.password = password1
                user.save()

            return redirect("users:login")
    # 초기 로드
    else:
        form = SignupForm()
        context = {
            "form" : form,
        }
    return render(request, "users/signup.html", context)