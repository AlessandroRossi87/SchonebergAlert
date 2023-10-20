from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# class Category(models.Model):
  name = models.CharField(max_length=255)

   class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, related_name='items',
                             on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True, default='No content')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
