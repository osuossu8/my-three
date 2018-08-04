
from os import environ #環境変数を取得

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

#########################################################

def iTunes_search(request):

    item_data = Singer.objects.all()

    lz = []
    ly = []

    tName_list = []
    kyoku_list = []

    sss = 0
    maxNum = "200"
    headers = {"content-type": "application/json"}

    for x in item_data:
        y = x.to_dict()
        z = x.__str__()
        lz.append(z)
        ly.append(y)

    sss = 0

    for v in lz:

        keyWord = v
        url_1 = 'https://itunes.apple.com/search?lang=ja&entry=music&media=music&country=JP&limit='+ maxNum +'&term=' + keyWord
        r1 = requests.get(url_1, headers=headers)
        data1 = r1.json()
        kyoku_list.append(data1["results"])

        #曲数だけ繰り返し、曲名のみを抽出する。
        eee = 0
        for ddd in kyoku_list[sss]:
            if lz[sss] == kyoku_list[sss][eee]["artistName"]: # DB内の歌手名とリスト内の曲の歌手名が一致した場合
                tName_list.append(kyoku_list[sss][eee]["trackName"])    #曲名を曲リストに追加する
            eee += 1
        sss += 1

    rrr = 0
    poyo = []

    for uuu in item_data:

        for ggg in tName_list:
            if ggg == ly[rrr]["goldSong"]:
                poyo.append(ggg)
                break
        for ggg in tName_list:
            if ly[rrr]["silverSong"] != "":
                if ggg == ly[rrr]["silverSong"]:
                    poyo.append(ggg)
                    break
        for ggg in tName_list:
            if ly[rrr]["bronzeSong"] != "":
                if ggg == ly[rrr]["bronzeSong"]:
                    poyo.append(ggg)
                    break
        rrr += 1

    aaa = 0
    hhh = 0
    ccc = []
    ppp = []
    qqq = []

    for uuu in item_data:

        for bbb in poyo:
            url_2 = 'https://itunes.apple.com/search?lang=ja&entry=music&media=music&country=JP&limit='+ maxNum +'&term=' + bbb
            r2 = requests.get(url_2, headers=headers)
            data2 = r2.json()
            aaa = 0
            if lz[hhh] == data2["results"][aaa]["artistName"]:
                ppp.append(data2["results"][aaa]["trackViewUrl"])
                qqq.append(data2["results"][aaa]["trackName"])
                ccc.append(data2["results"][aaa]["previewUrl"])
                aaa += 1
        hhh += 1

    kkk = []
    kkk.append(ppp)
    kkk.append(qqq)
    kkk.append(ccc)

    return render_json_response(request, kkk) #JSON

#########################################################

def youtube_search(request, song_name=None, singer=None):


    YouTube_API_KEY = environ["youtubeKey"]

    item_data = Singer.objects.all()


    ly = []
    lz = []
    length = len(item_data) #リストのサイズを取得する

    for x in item_data:
        y = x.to_dict()
        z = x.__str__()
        ly.append(y)
        lz.append(z)

    vId_list = []
    abc = 0
    headers = {"content-type": "application/json"}

    for ln in item_data:

        SINGER_NAME = lz[abc]
        SONG_NAME_1 = ly[abc]["goldSong"]
        SONG_NAME_2 = ly[abc]["silverSong"]
        SONG_NAME_3 = ly[abc]["bronzeSong"]



        if SONG_NAME_1 != "":
            url_1 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + " " + SONG_NAME_1  + "&type=videos"
            r1 = requests.get(url_1, headers=headers)
            data1 = r1.json()

            try:
                vId1 = data1["items"][1]["id"].get("videoId", None)
                if vId1 != None:
                    vId_list.append(vId1)
                    print(vId1)
                else:
                    url_1 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SONG_NAME_1  + "&type=videos"
                    r1 = requests.get(url_1, headers=headers)
                    data1 = r1.json()
                    vId1 = data1["items"][1]["id"].get("videoId", None)
                    vId_list.append(vId1)
                    print(vId1)

            except KeyError:
                return

        if SONG_NAME_2 != "":
            url_2 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + " " + SONG_NAME_2  + "&type=videos"
            r2 = requests.get(url_2, headers=headers)
            data2 = r2.json()

            try:
                vId2 = data2["items"][1]["id"].get("videoId", None)
                if vId2 != None:
                    vId_list.append(vId2)
                    print(vId2)
                else:
                    url_2 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SONG_NAME_2  + "&type=videos"
                    r2 = requests.get(url_2, headers=headers)
                    data2 = r2.json()
                    vId2 = data2["items"][1]["id"].get("videoId", None)
                    vId_list.append(vId2)
                    print(vId2)

            except KeyError:
                return
        else:
            print("no entry2")

        if SONG_NAME_3 != "":
            url_3 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + " " + SONG_NAME_3  + "&type=videos"
            r3 = requests.get(url_3, headers=headers)
            data3 = r3.json()

            try:
                vId3 = data3["items"][1]["id"].get("videoId", None)
                if vId3 != None:
                    vId_list.append(vId3)
                    print(vId3)
                else:
                    url_3 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SONG_NAME_3  + "&type=videos"
                    r3 = requests.get(url_3, headers=headers)
                    data3 = r3.json()
                    vId3 = data3["items"][1]["id"].get("videoId", None)
                    vId_list.append(vId3)
                    print(vId3)

            except KeyError:
                return
        else:
            print("no entry3")

        """
        if SONG_NAME_1 != "":
            url_1 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + SONG_NAME_1  + "&type=videos"
            r1 = requests.get(url_1, headers=headers)
            data1 = r1.json()
            vId1 = data1["items"][1]["id"]["videoId"]
            vId_list.append(vId1)

        if SONG_NAME_2 != "":
            url_2 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + SONG_NAME_2  + "&type=videos"
            r2 = requests.get(url_2, headers=headers)
            data2 = r2.json()
            vId2 = data2["items"][1]["id"]["videoId"]
            vId_list.append(vId2)
        else:
            print("no entry2")

        if SONG_NAME_3 != "":
            url_3 = "https://www.googleapis.com/youtube/v3/search?key=" + YouTube_API_KEY + "&part=snippet&q=" + SINGER_NAME + SONG_NAME_3  + "&type=videos"
            r3 = requests.get(url_3, headers=headers)
            data3 = r3.json()
            vId3 = data3["items"][1]["id"]["videoId"]
            vId_list.append(vId3)
        else:
            print("no entry3")
        """

        abc += 1

    print(vId_list)

    return render_json_response(request, vId_list) #JSON
