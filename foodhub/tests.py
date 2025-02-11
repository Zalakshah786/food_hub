# tests/test_models.py


from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from foodhub.models import Post, Chef_Comment
from foodhub.models import Dish_Receipe, MenuItem
from foodhub.models import CollaborateRequest, Post, Chef_Comment
from foodhub.models import MenuItem
from foodhub.forms import ChefCommentForm, CollaborateRequestForm

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            user=self.user,
            description='Test Description',
            content='Test Content',
            status=1
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(str(self.post), 'Test Post | by testuser')

class ChefCommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            user=self.user,
            status=1
        )
        self.comment = Chef_Comment.objects.create(
            user=self.user,
            post=self.post,
            text='Test Comment',
            rating=5
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test Comment')
        self.assertEqual(self.comment.rating, 5)
        self.assertFalse(self.comment.approved)

# tests/test_forms.py

class FormsTest(TestCase):
    def test_chef_comment_form_valid(self):
        form_data = {
            'text': 'Test Comment',
            'rating': 5
        }
        form = ChefCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_collaborate_request_form_valid(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test Message'
        }
        form = CollaborateRequestForm(data=form_data)
        self.assertTrue(form.is_valid())


class AdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client.login(username='admin', password='adminpass123')

    def test_post_admin(self):
        response = self.client.get(reverse('admin:foodhub_post_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_comment_admin(self):
        response = self.client.get(reverse('admin:foodhub_chef_comment_changelist'))
        self.assertEqual(response.status_code, 200)