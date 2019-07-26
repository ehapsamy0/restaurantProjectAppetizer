from django.shortcuts import render
from appetizer.models import Make_Reservation

# Create your views here.




def menu_det(request):
    return render(request,'menu.html',{})







def make_respons(request):#name email phone date time person
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        person = request.POST['person']
        make_reservation = Make_Reservation()
        make_reservation.name=name
        make_reservation.email=email
        make_reservation.phone=phone
        make_reservation.date=date
        make_reservation.time=time
        make_reservation.how_meny_person=person
        make_reservation.save()
        return HttpResponse('Done')


