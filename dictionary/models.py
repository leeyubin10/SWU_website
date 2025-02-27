from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)
