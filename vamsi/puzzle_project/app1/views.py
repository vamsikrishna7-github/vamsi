from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                return redirect('register')
            else:
                user=User.objects.create_user(username = username,password =password1, email = email)
                user.save()
                return redirect('login')
        else:
            return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):
    user = None
    if request.method=='POST':
        uname= request.POST.get('username')
        passwd = request.POST.get('pass')
        user = authenticate(username=uname, password=passwd)
    if user is not None:
        return redirect('home')
    else:
         return render(request, 'login.html')
   
def home(request):
    return render(request, 'home.html')
def logoutPage(request):
    logout(request)
    return redirect('login.html')