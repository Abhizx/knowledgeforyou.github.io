from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=130)
    url = models.CharField(max_length=80, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author