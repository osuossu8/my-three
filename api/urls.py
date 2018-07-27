
from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [

    path('v1/youtube_search/', views.youtube_search, name='youtube_search')
]
