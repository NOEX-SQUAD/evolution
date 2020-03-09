from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Novel


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register_form(request):
    return render(request, 'registerForm.html')


def login_form(request):
    return render(request, 'loginForm.html')


def novel(request):
    return render(request, 'novel.html')


def add_novel(request):
    return render(request, 'addNovel.html')


def create_account(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username นี้มีคนใช้แล้ว')
            return redirect('/createAccount')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'E-mail นี้มีคนใช้แล้ว')
            return redirect('/createAccount')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password
            )
            user.save()
            messages.info(request, 'ลงทะเบียนเรียบร้อยแล้ว')
            return redirect('/')
    else:
        messages.info(request, 'Password ไม่ตรงกัน')
        return redirect('/createAccount')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    # Login
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'ไม่พบข้อมูลผู้ใช้')
        return redirect('/signin')


def logout(request):
    auth.logout(request)
    return redirect('/')


def create_novel(request):
    name = request.POST['name']
    desc = request.POST['desc']

    createnovel = Novel.objects.create(
        name=name,
        desc=desc
    )
    createnovel.save()
    messages.info(request, 'บันทึกเรียบร้อยแล้ว')
    return redirect('/addNovel')
