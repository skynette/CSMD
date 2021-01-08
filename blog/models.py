from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class LikePost(models.Model):
    pass

class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    snippet = models.TextField(max_length=200, blank=True)
    content = models.TextField(max_length=5000, blank=True)
    comments = models.IntegerField(default=0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'title': self.title})


class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        "BlogPost", on_delete=models.CASCADE)

    def __str__(self):
        return self.content
