import sys
sys.dont_write_bytecode = True

from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Plan, PlanReply
from ..forms import PlanReplyForm

class PlanReplyView(LoginRequiredMixin, CreateView):
    model = PlanReply
    form_class = PlanReplyForm
    template_name = 'base/plan_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        reply = form.save(commit=False)

        plan_pk = self.kwargs['pk']
        plan = get_object_or_404(Plan, pk=plan_pk)

        reply.plan = plan
        reply.save()
        messages.success(self.request, '提出完了！')
        return redirect('base:plan-detail', pk=plan_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan'] = Plan.objects.get(pk=self.kwargs['pk'])
        return context