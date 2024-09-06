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