
from django.views import generic
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or another page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, "login.html")

def logout_view(request):
    logout(request)  # This will log the user out
    return redirect('home')  # Redirect to home or login page after logout

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})



def home_view(request):
    # Fetching all published posts
    posts = Post.objects.filter(status=1).order_by('-created_on')
    
    # Fetching comments for each post
    for post in posts:
        post.comments = Comment.objects.filter(post=post, approved=True)

    return render(request, 'index.html', {'posts': posts})
# Create your views here.
class Home(TemplateView):
    queryset = Post.objects.all()
    template_name = "foodhub/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # Add the posts to the context
        return context
    