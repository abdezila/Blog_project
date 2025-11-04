from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length= 500)

    class Meta:
        verbose_name = "Post"         
        verbose_name_plural = "Posts" 

    def __str__(self):
            return self.title