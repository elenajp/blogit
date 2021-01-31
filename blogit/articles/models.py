from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    # add thumbnail later
    # add author later

    def __str__(self):  # a built in function which defines how an article is going to look
        return self.title
