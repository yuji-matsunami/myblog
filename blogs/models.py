from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog_text = models.TextField()
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/', blank=True)
