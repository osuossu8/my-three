from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView

from .models import Singer, Song
from apps.forms import SingerForm,SongForm



def index(request, singer_id=None, song_id=None):

    if singer_id:
        singer = get_object_or_404(Singer, pk=singer_id)
    else:
        singer = Singer()

    if request.method == 'POST':
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            singer = form.save(commit=False)
            singer.save()
            return redirect('apps:index')
    else: # case GET is used
        form = SingerForm(instance=singer)

    latest_singer_list = Singer.objects.all().order_by('id')
    latest_song_list = Song.objects.all().order_by('id')[:3]
    context = {
        'latest_singer_list': latest_singer_list,
        'latest_song_list': latest_song_list,
        'form':form,
        'singer_id':singer_id
    }
    return render(request, 'apps/index.html', context)


def detail(request, singer_id):
    latest_singer_list = Singer.objects.all().order_by('id')[:5]
    latest_song_list = Song.objects.all().order_by('id')[:3]
    context = {
        'latest_singer_list': latest_singer_list,
        'latest_song_list': latest_song_list,
    }
    return render(request, 'apps/detail.html', context)

def results(request, singer_id):
    response = "You're looking at the results of singer %s."
    return HttpResponse(response % singer_id)

def vote(request, song_id):
    return HttpResponse("You're voting on song %s." % song_id)

def singer_del(request, singer_id):
    """曲の削除"""
    singer = get_object_or_404(Singer, pk=singer_id)
    singer.delete()

    return redirect('apps:index')
