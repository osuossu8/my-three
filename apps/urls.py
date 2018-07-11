from django.urls import path

from . import views


app_name='apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:singer_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:singer_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:singer_id>/vote/', views.vote, name='vote'),
    path('del/<int:singer_id>/', views.singer_del, name='singer_del'),
]
