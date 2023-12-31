from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
# Create your views here.

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }

    return render(request,'accounts_form.html',context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) #세션 
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }

    return render(request,'accounts_form.html',context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request,username):
    user_info = User.objects.get(username=username) # User안의 username 칼럼
    #nav.html의 {{user}}와 겹치기 않게함
    context = {
        'user_info':user_info
    }

    return render(request,'profile.html',context)

def follows(request, username):
    me = request.user # 팔로우 하는사람
    you = User.objects.get(username=username) # 팔로우 받는 대상

    #이미 팔로잉 되있는 경우
    # if me in you.followers.all():
    if you in me.followings.all():
        me.followings.remove(you)
    #팔로잉 안된경우      
    else:
        me.followings.add(you)

    return redirect('accounts:profile',username=username)