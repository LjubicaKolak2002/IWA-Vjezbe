from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Projection, Card
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import UserForm, ProjectionForm
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

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

    c1 = Card(num_seats = 1, projection = Projection.objects.get(pk=1), user = User.objects.get(pk=1))
    c2 = Card(num_seats = 1, projection = Projection.objects.get(pk=3), user = User.objects.get(pk=2))
    c3 = Card(num_seats = 1, projection = Projection.objects.get(pk=2), user = User.objects.get(pk=3))
    c4 = Card(num_seats = 1, projection = Projection.objects.get(pk=4), user = User.objects.get(pk=1))
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


@login_required
def get_projection(request):
    projection = Projection.objects.all()
    return render(request, 'projection.html', {"data":projection})


@login_required
def get_card(request, user_id):
    if request.user.id != user_id:
        return redirect('login')

    movies = Projection.objects.all()
    user_card = Card.objects.filter(user=user_id)
    return render(request, 'card.html', {"movies":movies, "user_card": user_card})


#vjezba 8
def register(request):
    if request.method == 'GET':
        userForm = UserCreationForm()
        return render(request, 'register.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            cleaned_data = userForm.cleaned_data
            print(cleaned_data)
            return redirect('login')
        else:
            return redirect('register')
    else:
        return HttpResponseNotAllowed('Nije se moguce registrirati!')


def check_login(request):
     if request.method == 'GET':
        userForm = UserForm()
        return render(request, 'login.html', {'form':userForm})
     elif request.method == 'POST':
        userForm = UserForm(request.POST)
        if request.user.is_authenticated and userForm.is_valid():
            userForm.save()
            cleaned_data = userForm.cleaned_data
            print(cleaned_data)
            return redirect('projection')
        else:
            return redirect('login')


def get_sold_projections(request):
    projection = Projection.objects.all()
    #projection1 = Projection.objects.get(id=3)
    #print(projection1.cards.all())

    if request.user.is_superuser:
        return render(request, 'sold_projection.html', {"data":projection})
    else:
        return HttpResponse("<h4>Samo zaposlenici mogu pristupiti trazenoj stranici...</h4>")
    

def get_user_by_card(request, movie_id):
    cards = Card.objects.filter(projection_id = movie_id)
    users = []

    movie_name = Projection.objects.get(pk=movie_id).film_name

    for card in cards:
        if User.objects.filter(id = card.user_id):
            if (User.objects.get(id = card.user_id).username) not in users: 
                users.append(User.objects.get(id = card.user_id).username)

    if request.user.is_superuser:
        return render(request, 'user_by_card.html', {"users":users, "film_name": movie_name})
    else:
         return HttpResponse("<h4>Samo zaposlenici mogu pristupiti trazenoj stranici...</h4>")


def update_projection(request, projection_id):
    projection_id = Projection.objects.get(id = projection_id)

    if request.user.is_superuser:
        if request.method == 'GET':
                projection_to_update = ProjectionForm(instance = projection_id)
                return render(request, 'update_projection.html', {'form': projection_to_update})
    
        elif request.method == 'POST':
            projection_to_update = ProjectionForm(request.POST, instance = projection_id)
            if projection_to_update.is_valid():
                projection_to_update.save()
                return redirect('projection')
        else:
            return HttpResponse("Dogodila se greska!")
    else:
        return HttpResponse('<h4>Samo zaposleni korisnici mogu azurirati projekcije!</h4>')



def delete_confirmation(request, projection_id):
    if request.user.is_superuser:
        if request.method == 'GET':
                return render(request, 'confirmation_delete.html', {"data":projection_id})
        return HttpResponseNotAllowed()
    
    else:
        return HttpResponse('<h4>Samo zaposleni korisnici mogu brisati projekcije!</h4>')


def delete_projection(request, projection_id):
    projection_by_id = Projection.objects.get(id = projection_id)
    print(request.POST)

    if 'da' in request.POST:
        projection_by_id.delete()
        return redirect('projection')
    else:
        return redirect('projection')

def add_projection(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            projectionForm = ProjectionForm()
            return render(request, 'add_projection.html', {'form': projectionForm})

        elif request.method == 'POST' and request.user.is_authenticated:
            projectionForm = ProjectionForm(request.POST)
            if projectionForm.is_valid():
                projectionForm.save()
                return redirect('projection')            
            else:
                return HttpResponseNotAllowed()
    else:
        return HttpResponse('<h4>Samo zaposleni korisnici mogu dodavati nove projekcije!</h4 >')
 
   


    
