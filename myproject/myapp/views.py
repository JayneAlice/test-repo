from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime 
from .models import Person

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def person_list(request):
    persons = Person.objects.all()
    
    return render(request,
                  "myapp/person/list.html",
                  {'persons': persons})

