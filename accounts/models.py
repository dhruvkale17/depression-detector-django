from django.db import models

# Create your models here.

class Tweet(models.Model):
    username = models.CharField(max_length=200, default="username")
    found = models.CharField(max_length=300)
    not_found = models.CharField(max_length=200)

    def __str__(self):
        return self.username + " " + self.tweet + " - " + self.depression