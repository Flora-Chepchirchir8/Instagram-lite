# from django.shortcuts import render,redirect,get_object_or_404
# from insta.models import Comment, Image, Profile
# from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
# from django.http.response import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives, send_mail
# from django.conf import settings
# from django.contrib import messages
# from django.urls import reverse

# @login_required
# def display_home(request):
#     Images = Image.get_images()
#     comments = Comment.get_comment()
#     profile = Profile.get_profile()
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = current_user
#             comment.save()
#         return redirect('home')

#     else:
#         form = CommentForm()

#     return render(request,"index.html",{"Images":Images, "comments":comments,"form": form,"profile":profile})












































































# # # Create your views here.
# # @login_required(login_url='/accounts/login/')
# # def display_home(request):

# #     posts = Image.objects.all()
# #     profile = Profile.objects.all()
# #     comment = Comment.objects.all()
# #     return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})


# # def signup(request):
# #     if request.method == 'POST':
# #         form = SignUpForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = request.POST['username']
# #             password = request.POST['password']
# #             email = request.POST['email']

# #             user = User.objects.create_user(username=username, email=email,password=password)
# #             subject = 'welcome to IC page'
# #             message = f'Hi {user.username}, thank you for registering in instagram clone.'
# #             email_from = settings.EMAIL_HOST_USER
# #             recipient_list = [user.email, ]
# #             send_mail( subject, message, email_from, recipient_list )
# #             return HttpResponse('Thank you for registering with us')
# #     else:
# #         form = SignUpForm()
# #     return render(request, 'registration_form.html', {'form': form})

# # def new_post(request):
   
# #     current_user = request.user
# #     profiles = Profile.objects.all()
# #     for profile in profiles:
# #         if profile.user.id == current_user.id:
# #             if request.method == 'POST':
# #                 form = NewPostForm(request.POST,request.FILES)
# #                 if form.is_valid():
# #                     upload = form.save(commit=False)
# #                     upload.posted_by = current_user
# #                     upload.profile = profile
# #                     upload.save()
# #                     return HttpResponseRedirect(reverse('home'))

# #             else:
# #                 form = NewPostForm()
# #             return render(request,'newpost.html',{"user":current_user,"form":form})            

# # @login_required(login_url='/accounts/login/')
# # def add_comment(request,id):
# #     post_comment = Comment.objects.filter(post= id)
# #     images = Image.objects.filter(id=id).all()
# #     current_user = request.user
# #     profile = Profile.objects.get(user = current_user)
# #     image = get_object_or_404(Image, id=id)
# #     if request.method == 'POST':
# #         form = CommentForm(request.POST)
# #         if form.is_valid():
# #             comment = form.save(commit = False)
# #             comment.post = image
# #             comment.user = profile
# #             comment.save()
# #             return HttpResponseRedirect(request.path_info)
# #     else:
# #         form = CommentForm()

# #     return render(request,'comments.html',{"form":form,"images":images,"comments":post_comment})

# # def show_profile(request):
# #     current_user= request.user
# #     images= Image.objects.filter(image_profile=current_user.id).all

# #     return render(request, 'registration/profile.html',{"images":images} )


# # # @login_required(login_url='/accounts/login/')    
# # # def update_profile(request):
# # #     current_user = request.user
# # #     if request.method == 'POST':
# # #         form = UpdateProfileForm(request.POST, request.FILES)
# # #         if form.is_valid():
# # #             profile = form.save(commit=False)
# # #             profile.user = current_user
# # #             profile.save()
# # #         return redirect('home')

# # #     else:
# # #         form = UpdateProfileForm()
# # #     return render(request, 'registration/profile.html', {"form": form})

# # @login_required(login_url='/accounts/login/')
# # def search(request): 
# #     if 'profile' in request.GET and request.GET['profile']:
# #         user = request.GET.get("profile")

# #         print(user)
# #         results = Profile.search_profile(user)
# #         message = f'profile'
# #         return render(request, 'search.html',{'profiles': results,'message': message})
# #     else:
# #         message = "You haven't searched for anything,try again"
# #     return render(request, 'search.html', {'message': message})


# # # def image_likes(request,id):
# # #     image =  Image.get_single_photo(id)
# # #     user = request.user
# # #     user_id = user.id
    
# # #     if user.is_authenticated:
    
# # #         image.save()
        
# # #     return redirect('index')

# # @login_required
# # def update_profile(request):
# #     if request.method == 'POST':
# #         # user_form = UpdateUserForm(request.POST, instance=request.user)
# #         profile_form =UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

# #         if profile_form.is_valid():
# #             # user_form.save()
# #             profile_form.save()
# #             messages.success(request, 'Your profile is updated successfully')
# #             return redirect(to='home')
# #     else:
# #         # user_form = UpdateUserForm(instance=request.user)
# #         profile_form =UpdateProfileForm(instance=request.user.profile)
# #     return render(request, 'registration/profile.html',{'profile_form': profile_form})