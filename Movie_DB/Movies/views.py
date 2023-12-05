from django.shortcuts import render, redirect

from Movies.models import Movie, Audience_Review
from Movies.forms import Movieform
from Crew.models import *
from Details.models import Genre
from Watchlist.models import Watchlist
from Details.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login,  logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
# importing date class from datetime module
from datetime import date
from django.core.paginator import Paginator




# Global keywords
current_year=str((date.today()).year)

# Create your views here.
def home(request):
    m  =  Movie.objects.all()
    filtered  =  Movie.objects.all()
    top  =  None
    popular  =  None
    theater  =  None
    if (request.method  == "GET"):
        popular = request.GET.get('popular')
        top = request.GET.get('top')
        theater = request.GET.get('theater')
    if top:
        filtered = Movie.objects.filter(rating__contains = 9)
    elif popular:
        filtered = Movie.objects.filter(Q(rating__icontains = 8))
    elif theater:
        filtered = Movie.objects.filter(year = current_year)
    return render(request, 'home.html',{'mov':m, 'filtered':filtered})


def register(request):
    if(request.method  == 'POST'):
        u = request.POST['username']
        m = request.POST['mail']
        p = request.POST['password']
        cp = request.POST['confirmpassword']
        if p == cp:
            user = User.objects.create_user(username=u, password=p)
            user.save()
            return home(request)
    return render(request, 'signup.html')
def usersignin(request):
    if(request.method  == 'POST'):
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user: #login only after authentication
            login(request, user)
            return home(request)
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')


def usersignout(request):
    logout(request)
    return home(request)



def view_movies(request):
    m = Movie.objects.all()
    # set up pagination
    p=Paginator(Movie.objects.all(),4)
    page = request.GET.get('page')
    movies=p.get_page(page)
    return render(request, 'movie_list.html', {'context':movies, 'context_count':m.count()})


@login_required
def add_movie(request):
    str = Streaming.objects.all()
    act = Actor.objects.all()
    dir = Director.objects.all()
    wri = Writer.objects.all()
    cin = Cinematographer.objects.all()
    cer = Certification.objects.all()
    if request.method  == "POST":
        name = request.POST['name']
        slug  =  (name.replace((' ' or ':'), '-')).lower()
        year = request.POST['year']
        release = request.POST['release']
        language = request.POST['language']
        rating = request.POST['rating']
        poster = request.FILES.get('poster')
        cover = request.FILES.get('cover')
        duration = request.POST['duration']
        ott = request.POST.get('ott')

        streaming = request.POST.get('streaming')
        actors = request.POST.getlist('actors')
        writers = request.POST.getlist('writers')
        cinematographer = request.POST.get('cinematographer')
        director = request.POST.get('director')

        trailer = request.POST['trailer']
        synopsis = request.POST['synopsis']
        movie  =  Movie.objects.create(user = request.user,  name = name,  slug = slug,  year = year,  release = release, 
                                         language = language,  rating = rating,  trailer = trailer, 
                                         poster = poster,  cover = cover,  duration = duration, 
                                         streaming_id = streaming,  ott = ott, 
                                         director_id = director,  cinematographer_id = cinematographer, 
                                         synopsis = synopsis)
        movie.save()
        for actor_id in actors:
            movie.actors.add(Actor.objects.get(id = int(actor_id)))
        for writer_id in writers:
            movie.writers.add(Writer.objects.get(id = int(writer_id)))
        return redirect('Movie:view_movies')
    else:
        pass
    return render(request, 'add_movie.html', {'streaming':str, 'certification':cer, 
                                            'actors':act, 'director':dir, 'writers':wri, 
                                            'cinematographer':cin, })
def delete_movie(request, mslug):
    try:
        movie = Movie.objects.get(slug = mslug)
        movie.delete()
        return render('delete.html', {'movie':movie})
    except:
        pass
    return redirect(request, 'Movie:view_movies')

class Delete_Movie(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url =  reverse_lazy('Movie:view_movies')

class Update_Movie(UpdateView):
    model = Movie
    template_name = 'add_movie.html'
    fields = ['name', 'year', 'release', 'rating', 'ott', 'poster', 'cover', 
            'certification', 'synopsis', 'trailer']
    success_url = reverse_lazy('Movie:view_movies')

def edit_movie(request, mslug):
    movie = Movie.objects.get(slug = mslug)
    form = Movieform(instance = movie)
    if request.method  == 'POST':
        form = Movieform(request.POST, request.FILES, instance = movie)
        if form.is_valid:
            form.save()
            return view_movie(request, mslug)
    return render(request, 'edit.html', {'edit':form,'movie':movie})

# def edit_movie(request, mslug):
#     movie = Movie.objects.get(slug = mslug)
#     if request.method  == 'POST':
#         movie.save()
#         return view_movie(request, mslug)
#     return render(request, 'edit.html', {'movie':movie})

def view_movie(request, mslug):
    user = request.user
    movie = Movie.objects.get(slug = mslug)
    watchlist = Watchlist.objects.filter(user = user, movie__slug = mslug)
    scores = Audience_Review.objects.filter(movie__slug = mslug, user = user)
    reviews = Audience_Review.objects.filter(movie__slug = mslug)
    related = Movie.objects.filter(Q(name = movie.name))
    # creating the date object of today's date
    return render(request, 'moviesingle.html', {'movie':movie, 'watchlist':watchlist,
                                            'review':reviews, 'review_count':reviews.count(),
                                            'scores':scores, 'related':related, 'count':related.count(),
                                            'current_year':current_year})


@login_required
def add_review(request, mslug):
    movie = Movie.objects.get(slug = mslug)
    if(request.method  == 'POST'):
        user = request.user
        title = request.POST.get('title')
        review = request.POST.get('review')
        score = request.POST.get('score')
        review = Audience_Review.objects.create(user = user, title = title, 
                                              review = review, movie = movie, score = score)
        if review:
            return render(request, 'add.html', {'movie':movie})
            review.save()
    else:
        pass
    return render(request, 'review.html', {'movie':movie})

class Delete_Review(Delete_Movie):
    model  =  Audience_Review
    template_name  =  'delete.html'
    context_object_name  =  'i'
    success_url  =  reverse_lazy('Movie:view_movies')

def delete_review(request,rslug):
    try:
        review=Audience_Review.objects.get(slug=rslug)
        review.delete()
    except:
        pass
    return redirect(request)

from rest_framework import viewsets
from Movies.serializers import MovieSerializer,UserSerializer
from Movies.models import Movie
from rest_framework.permissions import AllowAny
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny,]
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny,]
    queryset=User.objects.all()
    serializer_class = UserSerializer
