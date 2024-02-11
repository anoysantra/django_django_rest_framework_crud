from django.urls import path
from . import views

urlpatterns = [
    path('add_player/', views.add_cricketers, name='add_or_get_players'),

    path('get_player/',views.get_all_cricketers, name='get_all_players'),

    path('manipulate_bio/<int:player_id>', views.manipulate_player_bio , name= 'manipulate_bio'),

    path('manipulate_player_batting/<int:player_id>',views.manipulate_player_batting, name = 'manipulate_batting'),

    path('manipulate_player_bowling/<int:player_id>', views.manipulate_player_bowling, name = 'manipulate_bowling')

]