from Watchlist.models import Watchlist

def watchlist_status(request):
    pass


def watchlist_counter(request):
    watchlist_count=0
    if request.user.is_authenticated:
        user=request.user
        try:
            watchlist=Watchlist.objects.filter(user=user)
            watchlist_count=watchlist.count()
        except Movie.DoesNotExist:
            watchlist_count=0
        return {'watchlist_count':watchlist_count}
