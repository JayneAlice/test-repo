## zadanie 1
#### Otworzenie shell i import
``` python
>>> python manage.py shell
>>> from myapp.models import Person, Team
```
#### Dodawanie osób
``` python
>>> p1 = Person()
>>> p1.name = 'Peter'
>>> p1.shirt_size = 'M'
>>> p1.month_added = 4
>>> p1.age = 36
>>> p1.save()
```
``` python
>>> p2 = Person()
>>> p2.name = 'Iva'
>>> p2.shirt_size = 'L'
>>> p2.month_added = 6
>>> p2.age = 22
>>> p2.save()
```
``` python
>>> p3 = Person()
>>> p3.name = 'Levi'
>>> p3.shirt_size = 'S'
>>> p3.month_added = 1
>>> p3.age = 19
>>> p3.save()
```
#### Dodanie Teamów
``` Python
>>> t1 = Team()
>>> t1.name = 'Budda'
>>> t1.country = 'pl'
>>> t1.save()
```
``` Python
>>> t2 = Team()
>>> t2.name = 'Bazar'
>>> t2.country = 'us'
>>> t2.save()
```
``` Python
>>> t3 = Team()
>>> t3.name = 'Banshee'
>>> t3.country = 'uk'
>>> t3.save()
```
## zadanie 2
```python
>>> Person.objects.filter(name__startswith='A')
```
## zadanie 3
``` Python
>>> Person.bojects.filter(name__startswith='A').values('Team')
```
## zadanie 4
``` Python
>>> Persons = Person.objects.all()
```
## zadanie 5
#### Pierwsza osoba z listy
``` python
>>> Persons.first()
```
### Ostatnia osoba z listy
``` python
>>> Persons.last()
```
#### Od ostatniej osoby do pierwszej
```Python
>>> Persons.order_by('-name')
```
#### Co drugi element
```python
>>> Persons[::2]
```
## zadanie 6
```python
>>> Persons.exclude(team_id=0).count()
```
## zadanie 7
```python
>>> Team.objects.order_by("-name")
```
## zadanie 8
```python
>>> Team.objects.exclude(id__lt=3)
```
