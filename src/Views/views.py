from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth

# Create your views here.
def mainpage_view(request,*args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/Home")

        else:
            return HttpResponseRedirect("/Home")

    return render(request, "home.html", {"title":"Home Page"})