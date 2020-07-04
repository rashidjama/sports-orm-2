from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

from django.db.models import Q

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"all_leagues": League.objects.filter(name__contains  = "Baseball"),
		"wleagues": League.objects.filter(name__contains = "women"),
		"hockey_leagues": League.objects.filter(sport__contains = "hockey"),
		'allsports': League.objects.exclude(sport = "Football"),
		"conference_leagues": League.objects.filter(name__contains = "conference"),
		"all_atlantics": League.objects.filter(name__startswith="Atlantic"),
		"dallas_teams": Team.objects.filter(location__contains= "Dallas"),
		"raptors": Team.objects.filter(team_name="Raptors"),
		"city_teams": Team.objects.filter(location__endswith="city"),
		"t_teams": Team.objects.filter(team_name__istartswith="T"),
		"teams_locations": Team.objects.order_by('location'),
		"reverse_teams": Team.objects.order_by('-team_name'),
		"cooper_players": Player.objects.filter(last_name = "Cooper"),
		"ju_players": Player.objects.filter(first_name = "Joshua"),
		'coopers': Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexwyats": Player.objects.filter(Q(first_name="Alexander") |Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("/index")