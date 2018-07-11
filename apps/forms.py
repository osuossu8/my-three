from django import forms

from django.forms import ModelForm
from apps.models import Singer,Song


class SingerForm(ModelForm):
    """歌手のフォーム"""
    class Meta:
        model = Singer
        fields = ('singer_name','goldSong','silverSong','bronzeSong')

class SongForm(ModelForm):
    """曲のフォーム"""
    class Meta:
        model = Song
        fields = ('song_name','hitokoto',)
