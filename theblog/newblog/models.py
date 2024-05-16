from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    snippet = models.CharField(max_length=250)
    post_date = models.DateField(auto_now_add=True)
    body = RichTextField()

    def __str__(self):
        return self.title
        