# views.py

from django.shortcuts import render, redirect
from .forms import Client
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Client
from django.contrib import messages
def register_client(request):
    if request.method == 'POST':
        form = Client(request.POST)
        if form.is_valid():
            # Get the user agent from the request
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            # Get the client's IP address from the request
            ip_address = get_client_ip(request)
            # Save the user agent and IP address to the form before saving
            form.instance.useragent = user_agent
            form.instance.ip = ip_address

            form.save()  # Save the form data to the database
            return render(request,'success.html')  # Redirect to a success page after saving
    else:
        form = Client()
    return render(request, 'registration_form.html', {'form': form})


# Helper function to get client's IP address
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def rech(keyword):
    for client in Client.objects.all():
        if client.name == keyword:
            return client.age
    return False

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = str(rech(username))
        if age is not False:
            if age == password:
                return render(request,'success.html',{'name':username})
            else:
                return HttpResponse('<script>alert("Invalid Password") </script>')
        else:
            return HttpResponse('<script>alert("Invalid Client") </script>')

    return render(request, 'login.html')
def about(request):
    return  render(request,'about.html')
def index(request):
    return  render(request,'index.html')