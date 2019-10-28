from django.contrib import admin
from .forms import GameForm, PersonForm, PlayerForm
from .models import Game, Person, Player

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    form = GameForm

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm

admin.site.register(Game, GameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Player, PlayerAdmin)