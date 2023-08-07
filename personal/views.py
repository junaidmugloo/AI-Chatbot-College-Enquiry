from imaplib import _Authenticator
import json
from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .colab import utils
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from django.contrib.auth import logout, authenticate #add this
from django.contrib.auth import login as auth_login

def home_screen_view(request):
    print(request.headers)
    return render(request, "personal/home.html", {})


def chating_page(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        output = utils.runQuery(question)
        return render(request, "personal/chatting.html", {'answer': output})
    return render(request, "personal/chatting.html", {})

def signup(request):
     if request.method == 'POST':
        name=request.POST.get('name')
        emailid=request.POST.get('email')
        password=request.POST.get('password')
        #print(name,emailid,password)
        #return HttpResponse(json.dumps({"name":name, "email":emailid,"password":password}), content_type="application/json")
        if User.objects.filter(email = emailid).exists():
            messages.info(request,'Email already exists')
            return redirect('/')
        elif User.objects.filter(username = name).exists():
            messages.info(request,'username already exists')
            return redirect('/')
        else:
            user= User.objects.create_user(username=name,email=emailid,password=password)
            user.save();
            return redirect('/')




def login(request):
     if request.method == 'POST':
        pass1=request.POST['password']
        username=request.POST['username']
        
        user= authenticate(username=username,password=pass1)

        if user is not None:
            auth_login(request, user);
            #username1=user.username;
            #return render(request,"personal/chatting.html",{'uname':username1})
            request.session['username'] = user.username;
            return redirect('/chat/')   
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/')

def logout1(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect('chat')