from rest_framework import generics
from .models import members
from .serializers import MembersSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class MembersList(generics.ListCreateAPIView):
    queryset = members.objects.all()
    serializer_class = MembersSerializer
    permission_classes = [IsAuthenticated]


class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = members.objects.all()
    serializer_class = MembersSerializer
    permission_classes = [IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer