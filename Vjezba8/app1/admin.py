from django.contrib import admin
from .models import Projection, Card

# Register your models here.

class AdminProjection(admin.ModelAdmin):
    fields = ['film_name', 'film_time', 'capacity']
    list_filter = ['film_name']

admin.site.register(Projection, AdminProjection)

class AdminCard(admin.ModelAdmin):
    fields = ['num_seats', 'projection', 'user']

admin.site.register(Card, AdminCard)