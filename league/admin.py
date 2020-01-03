from django.contrib import admin
from .forms import GameForm, PersonForm, PlayerForm
from .models import (
    Game,
    Person,
    Player,
    Schedule,
    Role,
    PlayerStatistic,
    Team,
    TeamDetails,
    League,
    Injury,
    HistoryOfInjury,
)


class GameAdmin(admin.ModelAdmin):
    form = GameForm

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm

class ScheduleAdmin(admin.ModelAdmin):
    raw_id_fields = ['games',]
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Schedule, ScheduleAdmin)