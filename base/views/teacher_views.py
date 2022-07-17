import sys
sys.dont_write_bytecode = True

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings

from base.models import User

class StudentListView(ListView):
    model = User
    template_name = 'base/teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user
        context['students'] = teacher.student.all()
        return context