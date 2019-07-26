from django.shortcuts import render,get_object_or_404
from . import models
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        person = request.POST['person']
        make_reservation = models.Make_Reservation()
        make_reservation.name=name
        make_reservation.email=email
        make_reservation.phone=phone
        make_reservation.date=date
        make_reservation.time=time
        make_reservation.how_meny_person=person
        make_reservation.save()
        return HttpResponseRedirect('/')
    else:
        customers = models.HappyCustomer.objects.all()
        slider = models.Slider_title.objects.all()
        context = {
            'customers': customers,
            'slider':slider,

        }
    return render(request,'index.html',context)


