import datetime

from django.test import TestCase
from blog.models import Author, Blog, Comment
from django.contrib.auth.models import User

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Adnan', last_name='Khan', bio="Student")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')
    
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_first_name_comma_last_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name}, {author.last_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/blog/blogger/1')

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='Adnan', last_name='Khan', bio="Student")
        Blog.objects.create(title='TestTitle', content='TestText', pub_date_time=datetime.datetime.now(), author=author)

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_pub_date_time_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('pub_date_time').verbose_name
        self.assertEquals(field_label, 'pub date time')
        
    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_content_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('content').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEquals(expected_object_name, str(blog))

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEquals(blog.get_absolute_url(), '/blog/blog/1')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='1X<ISRUkw+tuK')
        author = Author.objects.create(first_name='Adnan', last_name='Khan', bio="Student")
        blog = Blog.objects.create(title='TestTitle', content='TestText', pub_date_time=datetime.datetime.now(), author=author)
        comment = Comment.objects.create(text='TestText', pub_date_time=datetime.datetime.now(), author=test_user, blog=blog)

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_pub_date_time_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('pub_date_time').verbose_name
        self.assertEquals(field_label, 'pub date time')
        
    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')
        
    def test_blog_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label, 'blog')

    def test_text_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_title(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = comment.text
        self.assertEquals(expected_object_name, str(comment))