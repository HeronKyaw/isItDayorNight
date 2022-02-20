from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    currentTime = int(now.strftime("%H"))
    return render(request, "dayornight/index.html", {
        "morning" : 6 < currentTime < 12,
        "afternoon" : 12 < currentTime < 17,
        "evening" : 17 < currentTime < 22,
        "night" : 22 < currentTime < 6
    })