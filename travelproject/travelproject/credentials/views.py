from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return  render(request,"login.html")



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        username1= request.POST['first_name']
        username2 = request.POST['last_name']
        username3 = request.POST['email']
        username4 = request.POST['password']
        username5= request.POST['password_again']

        if username4==username5:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('register')
            elif User.objects.filter(email=username3).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=username1, last_name=username2,
                                            email=username3, password=username4)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"new.html")
def logout(request):
    auth.logout(request)
    return redirect('/')