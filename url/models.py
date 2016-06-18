from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    url = models.URLField()
    site_name = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hashid = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    class Meta:
        ['-site_name']

    def __str__(self):
        return self.site_name


# class Click(models.Model):
    # url = models.URLField()
    # This model should track each time a url that is bookmarked is used.
