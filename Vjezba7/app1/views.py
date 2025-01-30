from django.shortcuts import render
from django.http import HttpResponse
from .models import Projection, Card
from django.contrib.auth.models import User

# Create your views here.

def welcome(request):
    return HttpResponse("Hello world!")

def get_data(request):
    """p1 = Projection(film_name="Home alone", film_time="15:00", capacity = 30)
    p2 = Projection(film_name="Batman", film_time="20:15", capacity = 120)
    p3 = Projection(film_name="Film3", film_time="19:30", capacity = 45)
    p4 = Projection(film_name = "Gentleman", film_time="19:25", capacity = 2)
    p5 = Projection(film_name = "Matrix", film_time = "17:15", capacity = 10)
    p5.save()
    p1.save()
    p2.save()
    p3.save()
    p4.save()

    c1 = Card(num_seats = 12, projection = Projection.objects.get(pk=32), user = User.objects.get(pk=1))
    c2 = Card(num_seats = 10, projection = Projection.objects.get(pk=35), user = User.objects.get(pk=2))
    c3 = Card(num_seats = 9, projection = Projection.objects.get(pk=33), user = User.objects.get(pk=3))
    c4 = Card(num_seats = 21, projection = Projection.objects.get(pk=34), user = User.objects.get(pk=1))
    c1.save()
    c2.save()
    c3.save()
    c4.save()"""

    return HttpResponse('Done...')
   


def buy_card(request, user_id, projection_id):
    movie = Projection.objects.get(id=projection_id)

    if movie.capacity == Card.objects.filter(projection=movie.id).count():
        return HttpResponse('<h4>Nije moguce kupiti kartu jer je popunjen kapacitet dvorane...</h4>')
        
    else:
        new_card  = Card(num_seats = movie.capacity - Card.objects.filter(projection=movie.id).count(), projection = Projection.objects.get(pk=projection_id), user = User.objects.get(pk=user_id))
        new_card.save()

    return render(request, 'card.html', {"movies": Projection.objects.all(), "user_card": Card.objects.filter(user=user_id)})


def get_projection(request):
    projection = Projection.objects.all()
    seats = {}
    for movie in projection:
        seats[movie.id] = movie.capacity - Card.objects.filter(projection=movie.id).count()

    return render(request, 'projection.html', {"data":projection, "free_seats": seats})
    


def get_card(request, user_id):
    movies = Projection.objects.all()
    user_card = Card.objects.filter(user=user_id)
    return render(request, 'card.html', {"movies":movies, "user_card": user_card})



