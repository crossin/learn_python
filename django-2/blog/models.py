from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


