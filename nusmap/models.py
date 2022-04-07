from django.db import models

# Create your models here.

# def get_file_path(request, filname):


class Category(models.Model):
    slug=models.CharField( max_length=150, null=False, blank=False)
    name=models.CharField( max_length=150, null=False, blank=False)
    imge=models.ImageField( upload_to=get_file_path, null=True, blank=True)