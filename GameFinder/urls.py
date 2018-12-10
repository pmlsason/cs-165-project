from django.urls import path
from . import views
"""
Patterns to make:
/GameFinder/users/<id>
/GameFinder/challenge
/GameFinder/Location
/GameFinder/Location/<id>
/GameFinder/messages
/GameFinder/players

"""

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view(), name='Users'),
    path('users/<int:id>', views.UserDetail.as_view(), name='User-Detail'),
    path('locations/', views.LocList.as_view(), name='Locations'),
    path('locations/<int:id>', views.LocationDetail.as_view(), name='Location-Detail'),
]
