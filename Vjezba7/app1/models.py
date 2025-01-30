from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projection(models.Model):
    film_name = models.CharField(max_length=30)
    film_time = models.CharField(max_length=30)
    capacity = models.IntegerField()

    def __str__(self):
        return ' %s %s' % (self.film_name, self.film_time)

class Card(models.Model):
    num_seats = models.IntegerField()
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE, blank=True, null=True, related_name = 'cards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name = 'cards')

    def __str__(self):
        return ' %s %s' % (self.num_seats, self.user)

