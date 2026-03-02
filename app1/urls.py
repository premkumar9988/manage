from django.urls import path
from .views import MembersList, MembersDetail

urlpatterns = [
    path('members/', MembersList.as_view()),
    path('members/<int:pk>/', MembersDetail.as_view()),
]