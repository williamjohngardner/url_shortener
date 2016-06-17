from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    url = models.URLField()
    site_name = models.CharField(max_length=60)
    description = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.site_name


class Click(models.Model):
    url = models.URLField()
    # This model should track each time a url that is bookmarked is used.
