from django.db import models

# Create your models here.

class Category(models.Model):
    slug=models.CharField( max_length=150, null=False, blank=False)
    name=models.CharField( max_length=150, null=False, blank=False)
    imge=models.ImageField( upload_to=None)