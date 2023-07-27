# views.py

from django.shortcuts import render, redirect
from .forms import ClientForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Client
from django.contrib import messages
from django.http import Http404
import  re
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            if not rechUser(username):  # I assume rechUser checks if the username already exists
                # Get the user agent from the request
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                # Get the client's IP address from the request
                ip_address = get_client_ip(request)

                # Save the user agent and IP address to the form before saving
                form.instance.useragent = user_agent
                form.instance.ip = ip_address
                form.save()  # Save the form data to the database
                return redirect('success')  # Redirect to a success page after saving
        else:
            return HttpResponse('<script> alert("Username already exists.")</script>')
    else:
        form = ClientForm()

    return render(request, 'registration_form.html', {'form': form})


# Helper function to get client's IP address
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def rechUser(keyword):
    verif = False
    for client in Client.objects.all():
        if client.name == keyword:
            verif  = True
            return True
    return verif
def rech(keyword):
    for client in Client.objects.all():
        if client.name == keyword:
            return client.age
    return False
def getUseragent(keyword):
    for client in Client.objects.all():
        if client.name == keyword:
            return client.useragent
    return False

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = str(rech(username))
        current_useragent = request.META.get('HTTP_USER_AGENT', '')
        user_agent = getUseragent(username)
        if age != 'False':
            if age == password:
                if user_agent == current_useragent :
                    return render(request, 'clientSpace.html', {'name': username,'age':age})
                else:
                    return render(request,'new_session.html',{'useragent':current_useragent,'IP':get_client_ip(request)})
            else:
                return HttpResponse('<script>alert("Invalid Password") </script>',status=404)
        else:
            return HttpResponse('<script>alert("Invalid Client") </script>',status=404)

    return render(request, 'login.html')
def about(request):
    return  render(request,'about.html')
def index(request):
    return  render(request,'index.html')
def success(request):
    if register_client(request)==None:
        return render(request,'registration_form.html')
    else:
        return render(request, 'success.html')
