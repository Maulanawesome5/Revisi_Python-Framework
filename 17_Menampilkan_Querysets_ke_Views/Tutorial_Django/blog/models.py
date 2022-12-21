from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    timePost = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.title}"
