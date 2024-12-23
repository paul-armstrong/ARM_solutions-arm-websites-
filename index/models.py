from django.db import models
from django.utils.text import slugify

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    help=models.TextField(blank=True,null=True)


class Service(models.Model):
    title=models.CharField(max_length=100)
    title_slug=models.SlugField(max_length=200,unique=True)
    top_header=models.TextField()
    content_header_1=models.TextField()
    content_header_2=models.TextField()
    content_header_3=models.TextField()
    content_header_4=models.TextField()
    content_text_1=models.TextField()
    content_text_2=models.TextField()
    content_text_3=models.TextField()
    content_text_4=models.TextField()


    def save(self,*args,**kwargs):
        self.title_slug=slugify(self.title)
        super().save(*args,**kwargs)

