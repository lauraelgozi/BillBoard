from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Posts, Comments
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView




# main funtion to render page
def index (request):

    # get form template for posts and comments
    postform = PostForm()
    commentform = CommentForm()


    posts = Posts.objects.filter(visible=True)

    logged_user = request.user


    return render(request, 'billboardapp/post.html', {'form': postform, 'commentform': commentform,
                                                      'posts': posts,
                                                      'user': logged_user })


# function to add new post to database
def addpost(request):
    if request.method == 'POST':

        form = PostForm(request.POST) 

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            # build data for response
            response_data = {}

            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = post.pk
            response_data['text'] = post.texts
            response_data['created'] = post.created_date.strftime('%B %d, %Y %I:%M %p')
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

# function to delete/make invisible specific post
@csrf_exempt
def deletePost(request):
    if request.method == 'POST':
        id = request.POST.get('postid')

        postToDelete = Posts.objects.get(pk=id)
        postToDelete.visible = False
        postToDelete.save()

        return HttpResponse(json.dumps({"Completed": "Post Removed"}),content_type="application/json")


# function to add comments to database
def addcomment(request):
    if request.method == 'POST':
        
        # get specific request
        ajaxdata = request.POST#.get('form')
   
        # add data to form
        form = CommentForm(ajaxdata) 
        
        if form.is_valid():

            specific_post = Posts.objects.get(pk=ajaxdata['postnumber'])
     
            commentpost = form.save(commit=False)
            commentpost.post_id = specific_post
            commentpost.save()
            
            # build response data for Ajax
            response_data = {}

            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = commentpost.pk
            response_data['text'] = commentpost.texts_comment

            # print(response_data)
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


# funtion to delete/make invisible comment from database
@csrf_exempt
def deleteComment(request):
    if request.method == 'POST':
        id = request.POST.get('commentid')
        print(id)

        commentToDelete = Comments.objects.get(pk=id)
        commentToDelete.visible = False
        commentToDelete.save()

        return HttpResponse(json.dumps({"Completed": "Comment Removed"}),content_type="application/json")


def registerUserPage(request):

    form =UserCreationForm()

    return render(request, 'registration/register.html', {'form': form })


def addUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            # get username and password for autologin
            username = request.POST['username']
            password = request.POST['password1']

            # #authenticate user then login
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            # redirect to main post view
            return redirect('../')
    else:
        form = UserCreationForm() 

    return render(request, 'registration/register.html', {'form': form})





class PostList(ListView):
    model = Posts
