from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date') # URL of the Post
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish_date',)

    def __str__(self):
        return f"Comment by {self.name}"
