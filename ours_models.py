class Game(models.Model):
    idgame = models.IntegerField(db_column='idGame', primary_key=True)  # Field name made lowercase.
    winner = models.CharField(max_length=45, blank=True, null=True)
    loser = models.CharField(max_length=45, blank=True, null=True)
    guest = models.CharField(max_length=45, blank=True, null=True)
    host = models.CharField(max_length=45, blank=True, null=True)
    date_match = models.CharField(max_length=45, blank=True, null=True)
    score_guest = models.CharField(max_length=45, blank=True, null=True)
    score_host = models.CharField(max_length=45, blank=True, null=True)
    final_score = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Game'



    class Meta:
        managed = False
        db_table = 'History of Injury'


class HistoryOfInjuryHasInjury(models.Model):
    history_of_injury_player_idplayer = models.ForeignKey(HistoryOfInjury, models.DO_NOTHING, db_column='History of Injury_Player_idPlayer', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    injury_idinjury = models.ForeignKey('Injury', models.DO_NOTHING, db_column='Injury_idInjury')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'History of Injury_has_Injury'
        unique_together = (('history_of_injury_player_idplayer', 'injury_idinjury'),)


class Injury(models.Model):
    idinjury = models.IntegerField(db_column='idInjury', primary_key=True)  # Field name made lowercase.
    date_of_accident = models.DateField(blank=True, null=True)
    break_time = models.IntegerField(blank=True, null=True)
    type_of_injury = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Injury'


class League(models.Model):
    idleague = models.IntegerField(db_column='idLeague', primary_key=True)  # Field name made lowercase.
    season = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'League'


class LeagueHasSchedule(models.Model):
    league_idleague = models.ForeignKey(League, models.DO_NOTHING, db_column='League_idLeague', primary_key=True)  # Field name made lowercase.
    schedule_idschedule = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='Schedule_idSchedule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'League_has_Schedule'
        unique_together = (('league_idleague', 'schedule_idschedule'),)


class LeagueHasTeam(models.Model):
    league_idleague = models.ForeignKey(League, models.DO_NOTHING, db_column='League_idLeague', primary_key=True)  # Field name made lowercase.
    team_idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='Team_idTeam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'League_has_Team'
        unique_together = (('league_idleague', 'team_idteam'),)


class Person(models.Model):
    idperson = models.IntegerField(db_column='idPerson', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'
        unique_together = (('idperson', 'user_iduser'),)


class Player(models.Model):
    idplayer = models.IntegerField(db_column='idPlayer', primary_key=True)  # Field name made lowercase.
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    person_idperson = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_idPerson')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Player'
        unique_together = (('idplayer', 'person_idperson'),)


class PlayerLicense(models.Model):
    player_idplayer = models.ForeignKey(Player, models.DO_NOTHING, db_column='Player_idPlayer', primary_key=True)  # Field name made lowercase.
    license_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player License'


class PlayerStatistic(models.Model):
    player_idplayer = models.ForeignKey(Player, models.DO_NOTHING, db_column='Player_idPlayer', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player Statistic'


class Role(models.Model):
    idrole = models.IntegerField(db_column='idRole', primary_key=True)  # Field name made lowercase.
    is_admin = models.CharField(max_length=45, blank=True, null=True)
    is_menager = models.CharField(max_length=45, blank=True, null=True)
    is_player = models.CharField(max_length=45, blank=True, null=True)
    person_idperson = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_idPerson')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'
        unique_together = (('idrole', 'person_idperson'),)


class Schedule(models.Model):
    idschedule = models.IntegerField(db_column='idSchedule', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'


class ScheduleHasGame(models.Model):
    schedule_idschedule = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='Schedule_idSchedule', primary_key=True)  # Field name made lowercase.
    game_idgame = models.ForeignKey(Game, models.DO_NOTHING, db_column='Game_idGame')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule_has_Game'
        unique_together = (('schedule_idschedule', 'game_idgame'),)


class Team(models.Model):
    idteam = models.IntegerField(db_column='idTeam', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    amount_of_wins = models.IntegerField(blank=True, null=True)
    amount_of_losses = models.IntegerField(blank=True, null=True)
    records = models.CharField(max_length=45, blank=True, null=True)
    founding_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'


class TeamDetails(models.Model):
    idteam_details = models.IntegerField(db_column='idTeam Details', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_color = models.CharField(max_length=45, blank=True, null=True)
    away_color = models.CharField(max_length=45, blank=True, null=True)
    arena_address = models.CharField(max_length=45, blank=True, null=True)
    team_idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team_idTeam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Team Details'
        unique_together = (('idteam_details', 'team_idteam'),)


class TeamHasGame(models.Model):
    team_idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team_idTeam', primary_key=True)  # Field name made lowercase.
    game_idgame = models.ForeignKey(Game, models.DO_NOTHING, db_column='Game_idGame')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Team_has_Game'
        unique_together = (('team_idteam', 'game_idgame'),)


class TeamHasPlayer(models.Model):
    team_idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team_idTeam', primary_key=True)  # Field name made lowercase.
    player_idplayer = models.ForeignKey(Player, models.DO_NOTHING, db_column='Player_idPlayer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Team_has_Player'
        unique_together = (('team_idteam', 'player_idplayer'),)


class User(models.Model):
    iduser = models.IntegerField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    is_auth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

