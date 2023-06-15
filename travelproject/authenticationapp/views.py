from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln = request.POST['lname']
        un = request.POST['uname']
        em = request.POST['email']
        ps = request.POST['pas']
        cnps = request.POST['cnpass']
        if ps==cnps:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username already exits ")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email already exits ")
                return redirect('register')
            else:
                authvar=User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=ps)
                authvar.save();
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
        return redirect('/')
    return render(request,"registration.html")



def login(request):
    if request.method=='POST':
        un=request.POST['uname']
        ps=request.POST['pass']
        user=auth.authenticate(username=un,password=ps)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
