from django.shortcuts import render
from django.http import JsonResponse
from . import data


def index(request):
    context = {}
    return render(request, "lobby/index.html", context)

def update(request):
    return JsonResponse(data.get(), safe=False)
