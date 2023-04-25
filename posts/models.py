from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9,decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.user.username}' - {self.post.title}
    
    