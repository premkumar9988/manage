from rest_framework import generics
from .models import members
from .serializers import MembersSerializer


class MembersList(generics.ListCreateAPIView):
    queryset = members.objects.all()
    serializer_class = MembersSerializer


class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = members.objects.all()
    serializer_class = MembersSerializer