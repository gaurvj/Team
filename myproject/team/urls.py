from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /team/
    url(r'^team/$', views.team, name='team'),

    # ex: /player/1/
    url(r'^player/(?P<team_id>\d+)/$', views.team_players, name='team_players'),

    # ex: /player_history/1/
    url(r'^player_history/(?P<player_id>[0-9]+)/$', views.players_history, name='players_history'),

    # ex: /point/1/
    url(r'^point/(?P<match_id>[0-9]+)/$', views.match_point, name='match_point'),
]