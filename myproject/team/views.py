from django.shortcuts import render
from team.models import *
from django.http import Http404


# Create your views here.

def team(request):
    try:
         team = Team.objects.all()
         matches = Match.objects.select_related()
         context = {'team': team, 'matches': matches}
    except Exception as e:
        print(e)
    return render(request, 'home.html', context)


def team_players(request, team_id):
    try:
        players = Player.objects.filter(team_id=team_id)
        team = Team.objects.get(id=team_id)
    except Player.DoesNotExist:
        raise Exception("team or player Doesn't Exist")
    return render(request, 'team_player_info.html', {'players': players, 'team': team})


def players_history(request, player_id):
    try:
        player = PlayerHistory.objects.filter(player_id=player_id)
        player_name = Player.objects.get(id=player_id)
    except PlayerHistory.DoesNotExist:
        raise Http404("player Doesn't Exist")
    return render(request, 'player_history.html', {'player': player, 'player_name': player_name})


def match_point(request, match_id):
    try:
        point = Point.objects.filter(match_id=match_id)
    except Match.DoesNotExist:
        raise Http404("match Doesn't Exist")
    return render(request, 'point.html', {'points': point})
