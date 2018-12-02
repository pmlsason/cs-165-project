from django.contrib import admin

# Register your models here.
from GameFinder.models import User, Player, Owner, Location
from GameFinder.models import Location_Sports, Location_Request, Game, Messages

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','FirstName','LastName','rating')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'Street', 'City')

admin.site.register(User, UserAdmin)
admin.site.register(Player)
admin.site.register(Owner)
admin.site.register(Location, LocationAdmin)
admin.site.register(Location_Sports)
admin.site.register(Location_Request)
admin.site.register(Game)
admin.site.register(Messages)
