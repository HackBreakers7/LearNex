from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('memorycard/', views.memmory_Card, name='memorygame'),
    path('canvas/', views.canvas, name='canvas'),
    path('connectdots/', views.connectdots, name='connectdots'),
    path('shapeselect/', views.shapeselect, name='shapeselect'),
    path('colorpick/', views.colorpick, name='colorpick'),
    path('math/', views.math, name='math'),
    path('orbit/', views.orbit, name='orbit'),
    path('subject/', views.subject, name='subject'),
    path('topic/', views.topic, name='topic'),
    path('track/', views.track, name='track'),
    path('quiz/', views.quiz, name='quiz'),
    path('books/', views.books, name='books'),
    path('rhym/', views.rhym, name='rhym'),
    path('video/', views.video, name='video'),
    path('animalgame/', views.animalgame, name='animalgame'),
        path('download/mathematics/', views.download_mathematics, name='download_mathematics'),
    path('download/science/', views.download_science, name='download_science'),
    path('download/history/', views.download_history, name='download_history'),
    path('download/geography/', views.download_geography, name='download_geography'),
# path('standard/', views.dashboard, name='dashboard'),
]
