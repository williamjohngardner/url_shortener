from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    url = models.URLField()
    site_name = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hashid = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    click_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.site_name


class Click(models.Model):
    url = models.ForeignKey(Url)
    created = models.DateTimeField(auto_now_add=True)
