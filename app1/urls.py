from django.urls import path
from .views import MembersList, MembersDetail,UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',UserCreate.as_view(),name='Create-User'),
    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('members/', MembersList.as_view()),
    path('members/<int:pk>/', MembersDetail.as_view()),
]