from django.shortcuts import render

# Create your views here.
def dashboard (request):
    return render(request,'dashboard.html')

def memmory_Card(request):
    return render(request,'memory card.html')

def canvas(request):
    return render(request,'canvas.html')

def connectdots(request):
    return render(request,'connectdots.html')

def shapeselect(request):
    return render(request,'shape selection.html')

def colorpick(request):
    return render(request,'colorpick.html')
def math(request):
    return render(request,'math.html')
def orbit(request):
    return render(request,'orbit.html')
def subject(request):
    return render(request,'subjects.html')
def topic(request):
    return render(request, 'topic.html')
def track(request):
    return render(request, 'track.html')
def quiz(request):
    return render(request, 'quiz.html')
def books(request):
    return render(request, 'books.html')

def rhym(request):
    return render(request, 'cargame.html')

def video(request):
    return render(request, 'video.html')

def animalgame(request):
    return render(request, 'animalgame.html')


from django.conf import settings
from django.http import FileResponse
import os

def download_mathematics(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/Part-1.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Part-1.pdf')

def download_science(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/science.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='science.pdf')

def download_history(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/history.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='history.pdf')

def download_geography(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'assets/geography.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='geography.pdf')
