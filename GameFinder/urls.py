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
    path('users/', views.UserListView.as_view(), name='Users'),
    path('users/<int:id>', views.User_detail.as_view(), name='User-Detail'),
    path('locations/', views.LocListView.as_view(), name='Locations'),
    path('locations/<int:id>', views.Location_detail.as_view(), name='Location-Detail'),
]
