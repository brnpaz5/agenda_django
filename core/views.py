from django.http import request, response
from django.shortcuts import render
from core.models import Event
# Create your views here.
def list_event(request):
    event = Event.objects.all()
    response = {'events': event}
    return render(request, 'agenda.html', response)