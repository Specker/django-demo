from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Parking, Parking_Slot, Enforcer

# Create your views here.
@login_required(login_url="/Home/")
def parking_detail_view(request):
    enforcer = Enforcer.objects.get(User=request.user)
    enforcers_parkings = enforcer.Parkings.all()
    parking_slots = Parking_Slot.objects.all()
    context = {
        "title": "Parking Details",
        "Parking_objects": enforcers_parkings,
        "Parking_slot_objects": parking_slots,
    }
    return render(request,"Parking/details.html",context)
