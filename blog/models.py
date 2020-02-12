from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, help_text='Title of your blog')
    content = models.TextField(max_length=2000, help_text='Content of your blog')
    pub_date_time = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', args=[str(self.id)])

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    pub_date_time = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text