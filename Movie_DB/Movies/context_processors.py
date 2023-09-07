from Movies.models import Movie

def movie_counter(request):
    movie_count=0
    if request.user.is_authenticated:
        user=request.user
        try:
            movies=Movie.objects.all()
            movie_count=movies.count()
        except Movie.DoesNotExist:
            movie_count=0
        return {'movie_count':movie_count}