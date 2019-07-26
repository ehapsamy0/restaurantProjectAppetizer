from django.db import models

# Create your models here.


class Slider_title(models.Model):
    title = models.CharField(max_length=200)
    slider_img = models.ImageField(upload_to='slider_img')


    def __str__(self):
        return self.title


class Make_Reservation(models.Model):
    name = models.CharField(max_length=150)
    email= models.EmailField()
    phone = models.IntegerField()
    date = models.CharField(max_length=50)
    time = models.TimeField()
    how_meny_person = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class HappyCustomer(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='cust_img')
    bio = models.TextField()
    cust_type = models.CharField(max_length=200)



    def __str__(self):
        return self.name
