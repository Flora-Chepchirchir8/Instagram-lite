from django.shortcuts import render,redirect,get_object_or_404
from .models import Comment, Image, Profile
from .forms import *
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

@login_required
def display_home(request):
    Images = Image.get_images()
    comments = Comment.get_comment()
    profile = Profile.get_profile()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()

    return render(request,"index.html",{"Images":Images, "comments":comments,"form": form,"profile":profile})

def profile(request,profile_id):
    try:
     profile = Profile.objects.get(pk=profile_id)

    except Profile.DoesNotExist:
      profile = None
    Images = Image.objects.filter(profile_id=profile).all()

    return render(request,"registration/profile.html",{"profile":profile,"Images":Images})


@login_required
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required
def search(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,"profiles":profile,"user":current_user,"username":searched_name})
    else:
        message = "You haven't searched for any username"
        return render(request,'search.html',{"message":message})


@login_required
def user_comments(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.poster = current_user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
        return render(request,{"user":current_user,"comment_form":form})

def follow(request,operation,id):
    current_user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,current_user)
        return redirect('home')

    elif operation=='unfollow':
        Follow.unfollow(request.user,current_user)
        return redirect('home')
        
def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('home')  


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         return redirect('home')
        
        else:
            messages.success(request,('Invalid information'))
            return redirect('login')
         
    else:

     return render(request,'registration/login.html')  

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register_user(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
         
            

             user = authenticate(username=username, password=password)
             login(request,user)

             messages.success(request,f'Hi {username}, Your account was created successfully .')
             return redirect('add_profile')
    else:
         form = UserRegisterForm()
    return render (request,'registration/registration_form.html',{'form':form})

def upload(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = UploadForm()
            return render(request,'upload.html',{"user":current_user,"form":form})







































































