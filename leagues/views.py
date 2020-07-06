from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

from django.db.models import Q

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"atlantic_teams": League.objects.filter(name__contains="Soccer"),
		"bostons":Team.objects.filter(team_name__istartswith="Penguins"),
		"cols":League.objects.filter(name__contains="Collegiate "),
		"amteures":League.objects.filter(name__contains="Amateur"),
		'ftplayers': League.objects.filter(name__contains="Football"),
		"evens": Player.objects.filter(first_name="Samuel"),
		"cats": Team.objects.filter(team_name="Tiger-Cats"),
		'vikings': Team.objects.filter(team_name="Vikings"),
		'jakes': Player.objects.filter(first_name="Jacob", last_name="Gray"),
		'joshes': League.objects.filter(name__contains="Amateur Baseball"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("/index")