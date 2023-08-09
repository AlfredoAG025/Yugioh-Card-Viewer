from django.shortcuts import render

import requests

url = "https://db.ygoprodeck.com/api/v7/randomcard.php"

payload = {}
headers = {}

def show_card_back(request):
    return render(request, 'card_back.html')


def show_card(request):
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    level_list = list(range(response['level'] if 'level' in response else 0))
    return render(request, 'card_viewer.html', {
        'response': response,
        'level_list': level_list
    })
