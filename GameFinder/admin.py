from django.contrib import admin

# Register your models here.
from GameFinder.models import Profile, Player, Owner, Location
from GameFinder.models import LocationSports, LocationRequest, Game, Messages

class UserAdmin(admin.ModelAdmin):
    list_display = ('profile_id','first_name','last_name','rating')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'street', 'city')

admin.site.register(Profile, UserAdmin)
admin.site.register(Player)
admin.site.register(Owner)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationSports)
admin.site.register(LocationRequest)
admin.site.register(Game)
admin.site.register(Messages)
