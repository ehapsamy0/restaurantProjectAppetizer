from django.shortcuts import render
from . import models
from appetizer.models import HappyCustomer
# Create your views here.



def index(request):
    chefs = models.MyChefs.objects.all()
    customers = HappyCustomer.objects.all()

    context = {
        'chefs':chefs,
        'customers':customers,

    }
    return render(request,'about.html',context)