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
# path('standard/', views.dashboard, name='dashboard'),
]
