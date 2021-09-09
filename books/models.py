from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
