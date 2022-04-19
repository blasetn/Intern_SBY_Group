from django.db import models, migrations
from django.contrib.auth.models import User


class Account(models.Model):
    phone = models.CharField(null=True, max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=250)
    sex = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=250)
    birthday = models.DateField(null=True)
    avatar = models.ImageField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=250)


class Post(models.Model):
    title = models.CharField(max_length=250)
    prince = models.FloatField()
    address = models.CharField(max_length=250)
    description = models.TextField(help_text='')
    type = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class ImagePost(models.Model):
    link = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class ImageNews(models.Model):
    link = models.ImageField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Feedback(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)


class Favorite(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
