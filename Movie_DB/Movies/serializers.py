from rest_framework import serializers
from Movies.models import Movie
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password']

    # def create(self,validated_data):
    #     user=User.objects.create(username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Token.objects.create(user=user)
    #     return user