from django.urls import path
from . import ui_views
from . import views


urlpatterns = [
    path('add_player/', views.add_cricketers, name='add_or_get_players'),

    path('get_player/', views.get_all_cricketers, name='get_all_players'),

    path('specific_player/<str:player_id>',
         views.get_specific_player, name='get_specific_player'),

    path('update_delete_cricketer/<str:player_id>',
         views.update_delete_cricketer, name='update_delete_cricketer'),

    path('get_manipulate_player_batting/<str:player_id>',
         views.manipulate_player_batting, name='get_manipulate_batting'),

    path('get_manipulate_player_bowling/<str:player_id>',
         views.manipulate_player_bowling, name='get_manipulate_bowling'),

    path('form_player/', ui_views.form_page, name='form_page'),

    path('show_data/', ui_views.show_page, name='show_players'),

    # path('debug/', views.debug, name='debug')

]
