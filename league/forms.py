from django.forms import ModelForm
from .models import Game, Person, Player


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('winner', 'loser', 'guest', 'host')

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('user', 'first_name', 'last_name', 'birthday_date')

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('person', 'height', 'weight')

