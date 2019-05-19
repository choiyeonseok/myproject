from django.utils import timezone

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    contents = models.TextField()
    photo = models.ImageField(blank=True, upload_to='product_photos')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def updated_at(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

