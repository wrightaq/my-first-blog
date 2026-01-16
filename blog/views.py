# view is where the logic of the application is put. Connect models and templates
# a view does:
# -receives the request information as well as parameters parsed from the url
# -fetches the information from the model, adds any other logic like sorting or filtering
# -creates a response by filling the corresponding template with the fetched info

from django.shortcuts import render, get_object_or_404, redirect #get_object_or_404 if a Post with the specified pk is not found will return a 404 Page not found
from django.utils import timezone
from .models import Post
from .forms import PostForm

# shows a list of published posts sorted by their published date
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts}) #render(info received from the user, template file, add info for the template to use)

# shows a single post containing title, text, and published date. If the user is admin it will also show icons for editing and deleting
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# shows a post form to fill out. It contain a space for a title and text. After submitted it will show the new post in post_detail
def post_new(request):
    if request.method == "POST": # saying if the form is filled out then continue onto validation, otherwise is a blank form
        form = PostForm(request.POST)
        if form.is_valid(): # check to see if everything is filled out correctly, should return True
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now() Removing this allows post to save as a draft instead of be published directly
            post.save()
            return redirect('post_detail', pk=post.pk) #pk stands for Primary Key and is an automated identifier field Django gives by default
    else:
        form = PostForm() # for creating a blank form
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk): #pk parameter needed to retrieve the specific post
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # the edited version
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now() Removing this allows post to save as a draft instead of be published directly
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) # the unedited version
    return render(request, 'blog/post_edit.html', {'form': form})

# takes only unpublished posts and orders them by created date
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')