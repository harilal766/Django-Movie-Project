from django.shortcuts import render,redirect
from Movies.models import Movie
from Movies.views import *
from Watchlist.models import Watchlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def view_watchlist(request):
    user=request.user
    watchlist=Watchlist.objects.filter(user=user) #filter based on user
    return render(request,'watchlist.html',{'watchlist':watchlist,'watchlist_count':watchlist.count()})
@login_required
def add_watchlist(request,p):
    user=request.user
    movie=Movie.objects.get(id=p)
    try:
        watchlist=Watchlist.objects.filter(movie=movie,user=user)
        if not watchlist.exists():
            watchlist=Watchlist.objects.create(user=user,movie=movie)
            watchlist.save()
        else:
            pass
    finally:
        return view_watchlist(request)
    return render(request,'watchlist.html')
@login_required
def delete_watchlist(request,p):
    user=request.user
    movie=Movie.objects.get(id=p)
    try:
        watchlist=Watchlist.objects.get(movie=movie,user=user)
        watchlist.delete()
    except:
        pass
    return redirect('Watchlist:view_watchlist')
