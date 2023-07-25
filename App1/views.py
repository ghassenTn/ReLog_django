# views.py

from django.shortcuts import render, redirect
from .forms import Client
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
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


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'success.html')  # Replace 'success' with the URL name of your success page
        else:
            error_message = "Invalid username or age."
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})