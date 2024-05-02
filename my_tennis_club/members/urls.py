from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name = 'main'),
    path('helo/', views.helo, name='helo' ),
    path ('members/', views.members, name = 'members'),
    path('members/details/<int:id>', views.details, name = 'details'),
    path('testing/', views.testing, name='testing'),
    path('table/', views.table, name = 'table'),
    path('firstname/', views.firstname , name = 'firstname')
]