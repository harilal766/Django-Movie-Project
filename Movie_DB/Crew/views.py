from django.shortcuts import render
from Crew.models import *
from Movies.models import *
# Create your views here.

def view_actor(request,aslug):
    context = Actor.objects.get(slug=aslug)
    filmography=Movie.objects.filter(actors__name=context.name)
    return render(request,'crew_detail.html',{'context':context,'filmography':filmography,
                                              'count':filmography.count()})
def view_director(request,dslug):
    context=Director.objects.get(slug=dslug)
    filmography=Movie.objects.filter(director__name=context.name)
    return render(request,'crew_detail.html',{'context':context,'filmography':filmography,
                                              'count':filmography.count()})
def view_writer(request,wslug):
    context=Writer.objects.get(slug=wslug)
    filmography = Movie.objects.filter(writers__name=context.name)
    return render(request, 'crew_detail.html',{'context': context, 'filmography': filmography,
                                               'count': filmography.count()})
def view_cinematographer(request,cslug):
    context=Cinematographer.objects.get(slug=cslug)
    filmography = Movie.objects.filter(cinematographer__name=context.name)
    return render(request, 'crew_detail.html',{'context': context, 'filmography': filmography,
                                               'count': filmography.count()})


from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from Crew.serializers import ActorSerializer
from Crew.models import Actor
class ActorViewSet(viewsets.ModelViewSet):
    permission_class=[AllowAny,]
    queryset=Actor.objects.all()
    serializer_class=ActorSerializer


