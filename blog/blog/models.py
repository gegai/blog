from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=64, unique=True)
    author = models.ForeignKey(User)
    head_img = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)
    alter_time = models.DateTimeField(auto_now=True)
    abstract = models.CharField('摘要', max_length=40, blank=True, null=True, help_text='默认摘取文章前40个字')
    content = RichTextField('内容')
    priority = models.IntegerField('优先级', default=100)
    category = models.ForeignKey('Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=26)
    alter_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class UserProfile(models.Model):
#     user = models.ForeignKey(User)
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
