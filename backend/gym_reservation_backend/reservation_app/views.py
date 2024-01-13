# reservation_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservation

def reserve_gym_slot(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Add code here to interact with your gym reservation bot
        # You can use the username and password to trigger the bot
        
        # Example: Save reservation details to the database
        Reservation.objects.create(username=username, password=password)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
