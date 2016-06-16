from django.db import models


class Url(models.Model):
    url = models.URLField()
    site_name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.site_name
