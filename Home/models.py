from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    link = models.TextField(max_length=255, default='')
    image = models.ImageField(null=True, blank=True,
                              upload_to='images/')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('sampleviewer')
