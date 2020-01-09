from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    INSTITUTION_TYPES = (
        (1, "foundation"),
        (2, "non-governmental organization"),
        (3, "local charity collection")
    )
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=1)
    categories = models.ManyToManyField(Category)
