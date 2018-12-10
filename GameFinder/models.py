from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_id = models.AutoField(primary_key=True)
    rating = models.DecimalField(decimal_places = 2, max_digits =3, default=0)
    first_name = models.CharField (max_length=16, help_text='Enter First Name') #different from phase 4
    last_name = models.CharField(max_length=16, help_text='Enter Last Name') #different from phase 4
    last_active = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.profile_id},{self.last_name}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('Profiles', args=[str(self.profile_id)])

class Player(models.Model):
    player = models.ForeignKey('Profile',on_delete=models.CASCADE) #on delete cascade??
    def __str__(self):
        return f'{self.player.profile_id},{self.player.last_name}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

"""
class PlayerSports(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    sports = models.CharField(max_length = 16)
"""
class Owner(models.Model):
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE) #on delete cascade?
    def __str__(self):
        return f'{self.owner.profile_id},{self.owner.last_name}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

"""
class Team(models.Model):
    team_id = models.AutoField()
    team_leader_id = models.ForeignKey(Player, player_id)
    team_name = models.CharField(max_length=32)

class TeamPlayers(models.Model):
    team_id = models.ForeignKey(Team, team_id)
    players = models.ForeignKey(Profile, first_name + last_name)

class TeamSports(models.Model):
    team_id = models.ForeignKey(Team, team_id)
    sports = models.CharField(max_length=16)
"""
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner',on_delete=models.CASCADE)
    name = models.CharField(max_length =32)
    street = models.CharField(max_length = 32)#different from phase 4
    city = models.CharField(max_length = 32) #different from phase 4
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('Locations', args=[str(self.location_id)])

class LocationSports(models.Model):
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    sports = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.location.name} - {self.sports}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player_challenge = models.ForeignKey('Player', related_name='challenger', on_delete=models.CASCADE)
    player_accept = models.ForeignKey('Player', related_name='accepter', on_delete=models.CASCADE)
    sport = models.CharField(max_length=16)
    date_time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.game_id

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

class LocationRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    def __str__(self):
        return f'{self.request_id} - {self.game} - {self.location}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

class Messages(models.Model):
    sender = models.ForeignKey('Profile', related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey('Profile',related_name='receiver', on_delete=models.CASCADE)
    text = models.CharField (max_length =256)
    date_time =  models.DateTimeField(auto_now =True)

    def __str__(self):
        return f'{self.sender}->{self.receiver}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

"""
class RateProfile(models.Model):
    rater_id = models.ForeignKey(Profile, profile_id)
    ratee_id = models.ForeignKey(Profile, profile_id)
    rating = models.DecimalField(decimal_places = 0, max_digits =1)
    date_time = models.DateTimeField(auto_now =True)

class StartGame(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    game_id = models.ForeignKey(Game, game_id)

class AcceptGame(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    game_id = models.ForeignKey(Game, game_id)

class AccommodateGame(models.Model):
    owner_id = models.ForeignKey(Profile, profile_id)
    game_id = models.ForeignKey(Game, game_id)

class RateLocation(models.Model):
    player_id = models.ForeignKey(Player, player_id)
    location_id = models.ForeignKey(Location, location_id)
    rating = models.DecimalField(decimal_places = 0, max_digits =1) """

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
