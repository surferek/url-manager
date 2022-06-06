from django.db import models


class UrlBind(models.Model):
    url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.short_url
