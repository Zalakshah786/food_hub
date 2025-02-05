
from django.views import generic
from .models import Post, Chef_Comment ,Dish_Receipe, MenuItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ChefRegistrationForm



import logging

logger = logging.getLogger('django')

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

def register_chef_view(request):
    if request.method == 'POST':
        form = ChefRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or another page
    else:
        form = ChefRegistrationForm()
    return render(request, 'register_chef.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, "login.html")

def logout_view(request):
    logout(request)  # This will log the user out
    return redirect('home')  # Redirect to home or login page after logout

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Chef_Comment.objects.filter(post=post)
    for comment in comments:
        comment.star_range = range(comment.rating)
    user_has_commented = False
    if request.user.is_authenticated:
        user_has_commented = Chef_Comment.objects.filter(post=post, user=request.user).exists()
    return render(request, 'foodhub/chef.html', {'post': post, 'comments': comments, 'user_has_commented': user_has_commented})

def dish_detail(request, pk):
    dish = Dish_Receipe.objects.get(pk=pk)
    return render(request, 'foodhub/dish_detail.html', {'pk': pk, 'dish': dish})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if Chef_Comment.objects.filter(post=post, user=request.user).exists():
        return redirect('post_detail', pk=pk)
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        rating = request.POST.get('rating', 0)  # Default to None if not provided
        comment = Chef_Comment(user=request.user, post=post, text=comment_text, rating=rating)
        comment.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'foodhub/chef.html', {'post': post})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Chef_Comment, pk=pk)
    if request.user != comment.user:
        return redirect('post_detail', pk=comment.post.pk)
    if request.method == 'POST':
        comment.text = request.POST.get('comment', '')
        comment.rating = request.POST.get('rating', 0)  # Default to 0 if not provided
        comment.save()
        return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'foodhub/chef.html', {'post': comment.post, 'edit_comment': comment})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Chef_Comment, pk=pk)
    if request.user != comment.user:
        return redirect('post_detail', pk=comment.post.pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'foodhub/chef.html', {'post': comment.post, 'delete_comment': comment})



def home_view(request):
    # Fetching all published posts
    posts = Post.objects.filter(status=1).order_by('-created_on')
    
    # Fetching all dishes
    dishes = Dish_Receipe.objects.all()
    
    # Fetching comments for each post
    for post in posts:
        post.comments = Chef_Comment.objects.filter(post=post, approved=True)

    return render(request, 'index.html', {'posts': posts,'dishes': dishes})
def menu_list(request):
    snacks_list = MenuItem.objects.filter(category='snacks').order_by('name')
    breakfast_list = MenuItem.objects.filter(category='breakfast').order_by('name')
    lunch_list = MenuItem.objects.filter(category='lunch').order_by('name')
    dinner_list = MenuItem.objects.filter(category='dinner').order_by('name')

    paginator_snacks = Paginator(snacks_list, 4)  # Show 4 snacks per page
    paginator_breakfast = Paginator(breakfast_list, 4)  # Show 4 breakfast items per page
    paginator_lunch = Paginator(lunch_list, 4)  # Show 4 lunch items per page
    paginator_dinner = Paginator(dinner_list, 4)  # Show 4 dinner items per page

    page_number_snacks = request.GET.get('page_snacks')
    page_number_breakfast = request.GET.get('page_breakfast')
    page_number_lunch = request.GET.get('page_lunch')
    page_number_dinner = request.GET.get('page_dinner')

    snacks = paginator_snacks.get_page(page_number_snacks)
    breakfast = paginator_breakfast.get_page(page_number_breakfast)
    lunch = paginator_lunch.get_page(page_number_lunch)
    dinner = paginator_dinner.get_page(page_number_dinner)

    context = {
        'snacks': snacks,
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
    }
    return render(request, 'foodhub/menu_list.html', context)
# Create your views here.
class Home(TemplateView):
    queryset = Post.objects.all()
    template_name = "foodhub/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # Add the posts to the context
        context['dishes'] = Dish_Receipe.objects.all()  # Add the dishes to the context
        return context
    










    
    