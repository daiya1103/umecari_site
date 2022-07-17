import sys
sys.dont_write_bytecode = True

from django.urls import path
from django.contrib.auth.views import LogoutView

from base.models.nippou import Nippou
from .views import (
    Index,
    MyLoginView,
    profileform,
    ProfileListView,
    ProfileDetailView,
    profileImageUpload,
    NippouListView,
    NippouCreateView,
    OutputListView,
    TagOutputListView,
    OutputCreateView,
    OutputDetailView,
    StudentListView,
)
app_name = 'base'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit', profileform, name='profile'),
    path('profile/icon/upload', profileImageUpload, name='icon-upload'),
    path('member/', ProfileListView.as_view(), name='profile-list'),
    path('member/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('nippou/', NippouListView.as_view(), name='nippou-list'),
    path('nippou/new/', NippouCreateView.as_view(), name='nippou-create'),
    path('output/', OutputListView.as_view(), name='output-list'),
    path('output/<str:slug>', TagOutputListView.as_view(), name='tagoutput-list'),
    path('output/new/', OutputCreateView.as_view(), name='output-create'),
    path('output/detail/<int:pk>/', OutputDetailView.as_view(), name='output-detail'),
    path('teacher/', StudentListView.as_view(), name='teacher'),
]