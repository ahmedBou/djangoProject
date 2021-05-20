import datetime

from django.shortcuts import render

# Create your views here.


def birthday(request):
    now = datetime.datetime.now()
    return render(request, "isMyBirthday/birthday.html", {
        "birth": now.month == 2 and now.day == 3
    })
