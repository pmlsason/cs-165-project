from django.shortcuts import render
from GameFinder.models import User, Player, Owner, Location
from GameFinder.models import Location_Sports, Location_Request, Game, Messages

# Create your views here.

def index(request):
    num_users = User.objects.all().count()
    num_locations = Location.objects.all().count()
    context = {'num_users': num_users, 'num_locations':num_locations}
    return render(request, 'index.html', context=context)

from django.views import generic

class UserListView (generic.ListView):
    model = User
#    context_object_name ='user_list'

class LocListView (generic.ListView):
    model = Location
#    context_object_name ='location_list'

class User_detail(generic.DetailView):
    model = User

class Location_detail(generic.DetailView):
    model= Location
