from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime,date

# Creation of profile model
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url=models.CharField(null=True,blank=True,max_length=255)
    facebook_url=models.CharField(null=True,blank=True,max_length=255)
    twitter_url=models.CharField(null=True,blank=True,max_length=255)
    instagram_url=models.CharField(null=True,blank=True,max_length=255)
    linkedin_url=models.CharField(null=True,blank=True,max_length=255)


    def __str__(self):
        return str(self.user)
        
    def get_absolute_url(self):
        return reverse('show_profile_page')

# creation of category model
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Post model
class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='uncategorized')
    snippet=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))

# comment model

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.post.id)))