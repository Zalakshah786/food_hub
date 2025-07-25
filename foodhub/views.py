from django.views import generic
from .models import Post, Chef_Comment, Dish_Receipe, MenuItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from .forms import ChefCommentForm, CollaborateRequestForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in!")
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def post_detail(request, pk):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, pk=pk)
    comments = Chef_Comment.objects.filter(
        post=post, approved=True).order_by("-created_at")
    comments_count = comments.count()
    comment_form = ChefCommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_form = ChefCommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Comment submitted and awaiting approval"
                )
                return redirect("post_detail", pk=pk)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "You must be logged in to submit a comment"
            )
            return redirect("account_login")

    user_has_commented = False
    if request.user.is_authenticated:
        user_has_commented = Chef_Comment.objects.filter(
            post=post, user=request.user
        ).exists()

    return render(
        request,
        "foodhub/chef.html",
        {
            "post": post,
            "comments": comments,
            "comments_count": comments_count,
            "comment_form": comment_form,
            "user_has_commented": user_has_commented,
        },
    )


def dish_detail(request, pk):
    dish = Dish_Receipe.objects.get(pk=pk)
    return render(
        request, "foodhub/dish_detail.html", {"pk": pk, "dish": dish})


@login_required
def edit_comment(request, pk, comment_id):
    """Edit a comment"""
    comment = get_object_or_404(
        Chef_Comment, pk=comment_id, post_id=pk, approved=True
    )
    
    # Check if user owns the comment
    if request.user != comment.user:
        return JsonResponse({"success": False, "message": "You can only edit your own comments"})
    
    if request.method == "POST":
        form = ChefCommentForm(request.POST, instance=comment)
        if form.is_valid():
            # Set approved to False after editing to require re-approval
            comment = form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment updated successfully and is awaiting approval"
            )
            return JsonResponse(
                {
                    "success": True,
                    "text": form.cleaned_data["text"],
                    "rating": form.cleaned_data["rating"],
                    "message": "Comment updated and awaiting approval"
                }
            )
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse(
        {"success": False, "message": "Invalid request method"})


@login_required
def delete_comment(request, pk, comment_id):
    """Delete a comment"""
    comment = get_object_or_404(
        Chef_Comment, pk=comment_id, post_id=pk, approved=True
    )

    if request.user == comment.user:
        if request.method == "POST":
            comment.delete()
            messages.add_message(
                request, messages.SUCCESS, "Comment deleted successfully"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Invalid request method"
            )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "You can only delete your own comments"
        )
    return HttpResponseRedirect(reverse("post_detail", args=[pk]))


def home_view(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    dishes = Dish_Receipe.objects.all()

    for post in posts:
        post.comments = Chef_Comment.objects.filter(post=post, approved=True)

    return render(request, "index.html", {"posts": posts, "dishes": dishes})


def menu_list(request):
    snacks_list = MenuItem.objects.filter(category="snacks").order_by("name")
    breakfast_list = MenuItem.objects.filter(
        category="breakfast").order_by("name")
    lunch_list = MenuItem.objects.filter(category="lunch").order_by("name")
    dinner_list = MenuItem.objects.filter(category="dinner").order_by("name")

    paginator_snacks = Paginator(snacks_list, 4)
    paginator_breakfast = Paginator(breakfast_list, 4)
    paginator_lunch = Paginator(lunch_list, 4)
    paginator_dinner = Paginator(dinner_list, 4)

    page_number_snacks = request.GET.get("page_snacks")
    page_number_breakfast = request.GET.get("page_breakfast")
    page_number_lunch = request.GET.get("page_lunch")
    page_number_dinner = request.GET.get("page_dinner")

    snacks = paginator_snacks.get_page(page_number_snacks)
    breakfast = paginator_breakfast.get_page(page_number_breakfast)
    lunch = paginator_lunch.get_page(page_number_lunch)
    dinner = paginator_dinner.get_page(page_number_dinner)

    context = {
        "snacks": snacks,
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
    }
    return render(request, "foodhub/menu_list.html", context)


class Home(TemplateView):
    queryset = Post.objects.all()
    template_name = "foodhub/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["dishes"] = Dish_Receipe.objects.all()
        return context


def collaborate_request_view(request):
    if request.method == "POST":
        form = CollaborateRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your collaboration request has been submitted successfully!"
                "I endeavour to respond within 2 working days."
            )
            return redirect("home")
    else:
        form = CollaborateRequestForm()
    return render(request, "collaborate_request.html", {"form": form})
