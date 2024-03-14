import requests
# from views import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CombinedDataForm
# the function to show all the cricketers data in the webpage


def show_page(request):

    response = requests.get('http://127.0.0.1:8000/api/get_player/')

    if response.status_code == 200:
        player_data = response.json()

        context = {
            'player_data': player_data,
        }

        return render(request, 'show_players.html', context)

    else:
        return HttpResponse("<h1>Problem in fetching Data</h1>")


def add_player(player_data):

    # pass the logic to input the data into the api.
    url = 'http://127.0.0.1:8000/api/add_player/'

    response = requests.post(url=url, json=player_data)

    if response.status_code == 200:
        print('Data Submitted Sucessfully')
    else:
        print('Failed to submit Data. Status Code :', response.status_code)
        print('Text: ', response.text)


def form_page(request):
    if request.method == 'POST':
        print('Working')
        form = CombinedDataForm(request.POST)

        if form.is_valid():
            print('Valid')
            cricketer_data = {key: form.cleaned_data[key] for key in [
                'player_id', 'jersey_no', 'name', 'team', 'total_matches_played']}

            cricketer_data['birthdate'] = str(form.cleaned_data['birthdate'])

            batting_data = {key: form.cleaned_data[key] for key in [
                'innings_played', 'total_runs', 'batting_style']}

            bowling_data = {key: form.cleaned_data[key] for key in [
                'innings_bowled', 'wickets_taken', 'bowling_style']}

            player_data = {
                'cricketer': cricketer_data,
                'batting': batting_data,
                'bowling': bowling_data
            }

            print(player_data)

            add_player(player_data)

            return HttpResponse("<h1>Data Submitted Successfully</h1>")
        else:
            print('Not Valid')
            print(form.errors)

    else:
        form = CombinedDataForm()

    return render(request, 'players_form.html', {'form': form})
