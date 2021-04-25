from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    thumbnail = models.ImageField(upload_to='uploads/images', null=False, blank=False)
    filename = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    aippackage = models.CharField(max_length=100, null=False, blank=False)
    size = models.CharField(max_length=10, null=False, blank=False)
    date = models.DateField(default=timezone.now)
    filetype = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.filename
