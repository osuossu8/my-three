import os import environ #環境変数を取得

import json
from django.http import HttpResponse
import requests

from apps.models import Singer,Song
from django.core import serializers
#from apps.config import youtubeKey  @local


def render_json_response(request, data, status=None):
    #response を JSON で返却
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def youtube_search(request, song_name=None, singer=None):


    YouTube_API_KEY = environ["youtubeKey"]

    item_data = Singer.objects.all()


    ly = []
    length = len(item_data) #リストのサイズを取得する

    for x in item_data:
        y = x.to_dict()
        ly.append(y)

    vId_list = []
    abc = 0
    headers = {"content-type": "application/json"}

    for ln in item_data:

        SONG_NAME_1 = ly[abc]["goldSong"]
        SONG_NAME_2 = ly[abc]["silverSong"]
        SONG_NAME_3 = ly[abc]["bronzeSong"]

        url_1 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q="  + SONG_NAME_1  + "&type=videos"
        url_2 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q="  + SONG_NAME_2  + "&type=videos"
        url_3 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q="  + SONG_NAME_3  + "&type=videos"

        r1 = requests.get(url_1, headers=headers)
        data1 = r1.json()
        vId1 = data1["items"][1]["id"]["videoId"]

        r2 = requests.get(url_2, headers=headers)
        data2 = r2.json()
        vId2 = data2["items"][1]["id"]["videoId"]
        r3 = requests.get(url_3, headers=headers)
        data3 = r3.json()
        vId3 = data3["items"][1]["id"]["videoId"]

        vId_list.append(vId1)
        vId_list.append(vId2)
        vId_list.append(vId3)
        print(vId_list)

        abc += 1

    return render_json_response(request, vId_list) #JSON
