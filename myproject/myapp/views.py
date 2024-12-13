from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse
import datetime 
from .models import Person, Team

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

# dodajemy brakujący import na początku pliku (modyfikacja)

def person_detail(request, id):
    # pobieramy konkretny obiekt Person
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "myapp/person/detail.html",
                  {'person': person})

def team_list(request):
    teams = Team.objects.all()

    return render(request,
              "myapp/team/list.html",
              {'teams': teams})


