from django.shortcuts import render
from django.http import HttpResponse
from GameFinder.models import Profile, Player, Owner, Location
from GameFinder.models import LocationSports, LocationRequest, Game, Messages

# Create your views here.

def index(request):
    num_users = Profile.objects.all().count()
    num_locations = Location.objects.all().count()
    context = {'num_users': num_users, 'num_locations':num_locations}
    return render(request, 'index.html', context=context)

def reg(request):
    return render(request, 'reg.html')

from django.views import generic

class UserList(generic.ListView):
    model = Profile
    #context_object_name ='user_list'

class LocList(generic.ListView):
    model = Location
    #context_object_name ='location_list'

class UserDetail(generic.DetailView):
    model = Profile

class LocationDetail(generic.DetailView):
    model = Location