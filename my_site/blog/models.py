import re
from tkinter import image_names
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_Name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email_adress=models.EmailField()
    
    def full_name(self):
        return f" {self.first_Name} {self.last_name}"


    def __str__(self):
        return self.full_name()
    
   
class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=200)
    # image_name= models.CharField(max_length=100) image upload field 
    image= models.ImageField(upload_to ="posts", null= True)
    date=models.DateField(auto_now=True)
    slug= models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author= models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tag=models.ManyToManyField(Tag)

class Comment(models.Model):
    username=models.CharField(max_length=25)
    email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")