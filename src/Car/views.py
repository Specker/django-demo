from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Car

# Create your views here.
@login_required(login_url="/Home/")
def car_detail_view(request):
    context = {
        "title": "Car Details",
        "Car_objects": Car.objects.all(),
    }
    return render(request,"Car/details.html",context)

@login_required(login_url="/Home/")
def car_drive_view(request,car_id, *args, **kwargs):
    car_object = Car.objects.get(id=car_id)
    car_object.status = 2
    car_object.driver = request.user
    car_object.save()
    context = {
        "title": "Car Details",
        "Car_object": car_object,
    }
    return render(request,"Car/drive.html",context)

