from django.db import models

# Create your models here.

class MyChefs(models.Model):
    name = models.CharField(max_length=90)
    name_jop = models.CharField(max_length=90)
    bio  = models.TextField()
    social_media_twitter = models.URLField(default='#',null=True,blank=True)
    social_media_instagram = models.URLField(default='#',null=True,blank=True)
    social_media_facebook = models.URLField(default='#',null=True,blank=True)
    social_media_google = models.URLField(default='#',null=True,blank=True)
    img = models.ImageField(upload_to='about/chefs',null=True,blank=True)

    def __str__(self):
        return self.name