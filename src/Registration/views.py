from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email','')
        if password == password2:
            user = User.objects.create_user(username, email, password)

            user.first_name = fname
            user.last_name = lname
            user.save()
            user = auth.authenticate(username=username, password=password)
        else:
            return render(request,"Register/register.html",{})

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/Home")
        else:
            return HttpResponseRedirect("/Home")

    return render(request,"Register/register.html",{})

