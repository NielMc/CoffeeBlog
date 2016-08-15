from django.test import TestCase
from .models import Post
from blog.views import blog_posts
from blog.views import post_detail
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User

# Create your tests here.
class PostTests(TestCase):
    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(
            str(test_title),
            'My Latest Blog Post'
        )

class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1,1)

class PostListTest(TestCase):
    def test_blog_page_resolves(self):
        blog_page = resolve('/blog/')
        self.assertEqual(blog_page.func, blog_posts)

    def test_blog_page_status_code_is_ok(self):
        index = self.client.get('/')
        self.assertEqual(index.status_code, 200)

class PostDetailsTest(TestCase):

    fixtures = ['posts','users']
    def test_details_page_resolves(self):
        blogdetail_page = resolve('/blog/1/')
        self.assertEqual(blogdetail_page.func, post_detail)

class HomePageTest(TestCase):

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser@example.com')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser@example.com',password='letmein')
        self.assertEqual(self.login,True)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user':self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)
