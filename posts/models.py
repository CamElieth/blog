from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

#creando modelo de nuestro user
class User(AbstractUser):
    pass
    
    def str(self):
        return self.username
    

#Creando mdelo post.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
     
    def str(self):
         return self.title
     
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def get_like_url(self):
        return reverse("like", kwargs={"slug": self.slug})
    
    @property
    def comment(self):
        return self.comment_set.all()
    
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()
    
     
#Creando modelo para comentarios.
class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str_(self):
        return self.user.username
    
  
# Creando modelo para vista del post.
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models. CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str_(self):
        return self.user.username

#Creando modelo para likes en las publicaciones.
class Like (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models. CASCADE)
    
    def str(self):
        return self.user.username

# Create your models here.
class PostFot (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models. CASCADE)
    
    def str(self):
        return self.user.username