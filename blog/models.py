from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from slugify import slugify
# Create your models here.


class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey("BlogPost", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class LikePost(models.Model):
    pass

class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    snippet = models.TextField(max_length=200, blank=True)
    content = models.TextField(max_length=5000, blank=True)
    comments = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'title': self.title})
    
    @property
    def get_comments(self):
        return CommentPost.objects.filter(post=self).count()

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

