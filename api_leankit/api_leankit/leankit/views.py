from django.shortcuts import render
import requests
import json
from django.http import JsonResponse


def archive(request):

    username = 'juliana.goncalves@corp.globo.com'
    password = 'Admin1234'
    url_api = "https://produtos-globocom.leankit.com/kanban/api/board/196166479/archive"

    http = requests.Session()
    http.auth = (username, password)
    response = http.get(url_api)  # string json

    board_datas = json.loads(response.content)  # dicionario python

    cards_esp2 = board_datas['ReplyData'][0][0]['ChildLanes'][2]['Lane']['Cards']

    title = board_datas['ReplyData'][0][0]['ChildLanes'][2]['Lane']['Title']

    context = {
        'title': title,
        'cards': cards_esp2
    }

    return render(request, 'board.html', context)
    # return JsonResponse(context)
