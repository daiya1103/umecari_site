import sys
sys.dont_write_bytecode = True

import base64
import numpy as np
import os
import pandas as pd

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_pandas.io import read_frame

from base.forms import ProfileForm
from base.models import User, Profile, Nippou

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'base/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了！')
        return super().form_valid(form)

@login_required
def profileform(request):
    profile = request.user.profile
    icon = profile.icon
    dream = profile.dream
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            if not profile.icon:
                profile.icon = icon
            if not profile.dream:
                profile.dream = dream
            profile.save()
            print(profile.dream)
            messages.success(request, 'プロフィールが変更されました')
            return redirect('base:index')
    else:
        form = ProfileForm(request.POST, request.FILES)
    return render(request, 'base/profile_form.html', {'form': form})

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'base/profile_list.html'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'base/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        user_nippou =  Nippou.objects.filter(user=profile.user).values('revenue','date').order_by('date')
        df_nippou = read_frame(user_nippou)
        df_nippou['date'] = pd.to_datetime(df_nippou['date'])
        mm = df_nippou.set_index(['date'])
        all_sum_of_revenue = mm.resample(rule='M').sum()
        sum_of_revenue_list = all_sum_of_revenue['revenue'].tolist()
        if not len(sum_of_revenue_list) == 0:
            sum_of_revenue = sum_of_revenue_list[-1]
        else:
            sum_of_revenue = 0
        context['sum_of_revenue'] = sum_of_revenue
        return context
