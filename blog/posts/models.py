from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    image = models.ImageField(upload_to='image', blank=True)


    def __str__(self):
        return self.title