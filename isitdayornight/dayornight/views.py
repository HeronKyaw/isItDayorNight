from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    currentTime = int(now.strftime("%H"))
    return render(request, "dayornight/index.html", {
        "dayornight" : currentTime < 12 and currentTime > 12
    })