from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Post,Comment
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def register_user(request):
    page = "register"
    form = UserCreationForm()
    context = {
        "form":form,
        "page":page,
    }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"something went wrong")
            # return render(request,"blog/register_user.html",context)
    return render(request,"blog/register_user.html",context)

def login_view(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"user does not exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"username or password does not exist")

    context = {"page":page}
    return render(request,"blog/register_user.html",context)


def logout_view(request):
    logout(request)
    return redirect("home")
def home(request):
    posts = Post.objects.all().order_by("-pub_date")
    context = {
        "posts":posts
    }
    return render(request,"blog/home.html",context)

@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        user = request.user
        if title == "" or body == "":
            messages.error(request,"You did not enter anything in title or body field!")
            return redirect("create-post")
        Post.objects.create(user=user,body=body,title=title)
        return redirect("home")
    form  =PostForm()
    return render(request,"blog/create_post.html",{"form":form})

@login_required(login_url="login")
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    try:
        referer = request.META['HTTP_REFERER']
    except KeyError:
        referer = "http://127.0.0.1:8000/home"
    if request.user != post.user:
        return redirect("home")
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request,"blog/delete_post.html",{"obj":post,"referer":referer})


def view_post(request,pk):
    post = Post.objects.filter(id=pk).first()
    context = {'post':post}
    return render(request,"blog/view_post.html",context)