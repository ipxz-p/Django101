from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .models import User
from .serializer import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
