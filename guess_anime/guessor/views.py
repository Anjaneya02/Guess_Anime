from django.shortcuts import render
from django.http import HttpResponse
import random
from AnilistPython import Anilist
# Create your views here.

def first(request):
    anilist = Anilist()
    l=anilist.search_anime(genre=['Slice of Life'], score=range(80, 95))

    r=random.randint(0,len(l))
    selected=l[r]
    return render(request,'index.html',selected)