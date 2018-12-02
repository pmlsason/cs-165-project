from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField()
    rating = models.DecimalField(decimal_places = 2, max_digits =3)
    FirstName = models.CharField (max_length=16, help_text='Enter First Name') #different from phase 4
    LastName = models.CharField(max_length=16, help_text='Enter Last Name') #different from phase 4
    last_active = models.DateTimeField(auto_now=True)
"""
class Player(models.Model):
    player_id = models.ForeignKey(User,id) #on delete cascade??

class Player_Sports(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    sports = models.CharField(max_length = 16)

class Owner(models.Model):
    owner_id = models.ForeignKey(User, id) #on delete cascade?

class Team(models.Model):
    team_id = models.AutoField()
    team_leader_id = models.ForeignKey(Player, player_id)
    team_name = models.CharField(max_length=32)

class TeamPlayers(models.Model):
    team_id = models.ForeignKey(Team, team_id)
    players = models.ForeignKey(User, FirstName + LastName)

class TeamSports(models.Model):
    team_id = models.ForeignKey(Team, team_id)
    sports = models.CharField(max_length=16)

class Location (models.Model):
    location_id = models.AutoField()
    owner_id = models.ForeignKey(Owner, owner_id)
    name = models.CharField(max_length =32)
    Street = models.CharField(max_length = 32)#different from phase 4
    City = models.CharField(max_length = 32) #different from phase 4

class Location_Sports (models.Model):
    location_id = models.ForeignKey(Location, location_id)
    sports = models.CharField(max_length=16)

class Game(models.Model):
    game_id = models.AutoField()
    player_challenge = models.ForeignKey(Player, player_id)
    player_accept = models.ForeignKey(Player, player_id)
    sport = models.CharField(max_length=16)
    date_time = models.DateTimeField(auto_now = True)


class Location_Request(models.Model):
    request_id = models.AutoField()
    game_id = models.ForeignKey(Game, game_id)
    location_id = models.ForeignKey(Location, location_id)
    date_time = models.DateTimeField(auto_now =True)

class Messages(models.Model):
    sender_id = models.ForeignKey(User, user_id)
    receiever_id = models.ForeignKey(User, user_id)
    text = models.CharField (max_length =256)
    date_time =  models.DateTimeField(auto_now =True)

class Rate_User(models.Model):
    rater_id = models.ForeignKey(User, user_id)
    ratee_id = models.ForeignKey(User, user_id)
    rating = models.DecimalField(decimal_places = 0, max_digits =1)
    date_time = models.DateTimeField(auto_now =True)

class StartGame(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    game_id = models.ForeignKey(Game, game_id)

class AcceptGame(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    game_id = models.ForeignKey(Game, game_id)
class AccommodateGame(models.Model):
    owner_id = models.ForeignKey(User, user_id)
    game_id = models.ForeignKey(Game, game_id)
class RateLocation(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    location_id = models.ForeignKey(Location, location_id)
    rating = models.DecimalField(decimal_places = 0, max_digits =1) """
