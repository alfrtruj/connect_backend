from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    thumbnail = models.ImageField(upload_to='uploads/images', null=False, blank=True)
    filename = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField()
    aippackage = models.CharField(max_length=100, null=False, blank=True)
    size = models.CharField(max_length=10, null=False, blank=True)
    date = models.DateField(default=timezone.now)
    filetype = models.CharField(max_length=50, null=False, blank=True)


    def __str__(self):
        return self.filename
