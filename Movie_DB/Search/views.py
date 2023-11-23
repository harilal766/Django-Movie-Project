from django.shortcuts import render
from Movies.models import Movie
from django.db.models import Q
from Details.models import Genre
from Crew.models import Actor
from django.contrib import messages
# Create your views here.
def searchmovie(request):
    movie=None
    actor=None
    query=None
    if request.method=="GET":
        query = request.GET.get("query")
        check=Movie.objects.get(Q(name__icontains=query))
        if query:
            movie=Movie.objects.filter(Q(name__icontains=query))
            # return render(request,'searchresult.html',{'query':query,'movie':movie,'count':movie.count(),'check':check})
        # if query and query==check:
        #     movie=Actor.objects.filter(Q(name__icontains=query))
        #     return render(request,'searchresult.html',{'query':query,'actor':movie,'count':movie.count(),'check':check})
        else:
            pass
    return render(request,'searchresult.html',{'query':query,'movie':movie,'count':movie.count(),'check':query})


# def searchmovie(request):
#     movie=None
#     if request.method=="GET":
#         query = request.GET.get("query")
#         check=Movie.objects.filter(Q(name__icontains=query))
#         if query in check:
#             movie=Movie.objects.filter(Q(name__icontains=query))
#             return render(request,'searchresult.html',{'query':query,'result':movie,'count':movie.count()})
#         elif query not in check:
#             movie=Actor.objects.filter(Q(name__icontains=query))
#     return render(request,'crew_searchresult.html',{'query':query,'result':movie,'count':movie.count()})

def advanced_search(request):
    movie_query=None
    genre_query = None
    rating_query = None
    from_query = None
    to_query = None
    movie=None
    if request.method=='GET':
        movie_query=request.GET.get('movie_query')
        genre_query=request.GET.get('genre_query')
        rating_query=request.GET.get('rating_query')
        from_query=request.GET.get('from_query')
        to_query=request.GET.get('to_query')
        if movie_query:
            movie=Movie.objects.filter(Q(name__icontains=movie_query))
        elif genre_query:
            movie=Movie.objects.filter(Q(genres__name__icontains=genre_query))
        elif rating_query:
            movie = Movie.objects.filter(Q(rating__contains=rating_query))
        elif from_query :
            movie = Movie.objects.filter(Q(year__icontains=from_query))
        elif to_query :
            movie = Movie.objects.filter(Q(year__icontains=to_query))
        elif from_query and to_query :
            movie = Movie.objects.filter(Q(year__icontains=from_query and to_query))
            # movie = Movie.objects.filter(Q(year__icontains=to_query)|Q(year__icontains=from_query))
        else:
            pass
    return render(request,'searchresult.html',{'query':movie_query or genre_query or rating_query or from_query or to_query,
                                                     'movie':movie,
                                                     'count':movie.count(),
                                                     })
