import datetime
from django.db import models
from django.utils import timezone

class Singer(models.Model):
    singer_name = models.CharField(max_length=50)
    #pub_date = models.DateTimeField('date published')
    goldSong = models.CharField(max_length=50,blank=True)
    silverSong = models.CharField(max_length=50,blank=True)
    bronzeSong = models.CharField(max_length=50,blank=True)
    hitokoto = models.CharField(max_length=50,blank=True)
    sore = models.IntegerField(default=0)

    def __str__(self):
        return self.singer_name

    ### Djangoモデル を python辞書に変換する
    def to_dict(self):

        return {  "goldSong"  : self.goldSong,
                  "silverSong": self.silverSong,
                  "bronzeSong": self.bronzeSong,
                }

class Song(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=50)
    hitokoto = models.CharField(max_length=50,blank=True)
    sore = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
