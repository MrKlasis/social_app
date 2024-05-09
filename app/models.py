from django.db import models
from .validators import validate_password, validate_email_domain, validate_author_age, validate_title


class User(models.Model):
    email = models.CharField(max_length=50, validators=[validate_email_domain])
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50, validators=[validate_password])
    number = models.CharField(max_length=15)
    date_of_birth = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, validators=[validate_author_age])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
