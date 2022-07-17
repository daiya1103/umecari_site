import sys
sys.dont_write_bytecode = True

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from base.forms import ProfileForm
from base.models import User, Profile, Output, OutputTagModel

class OutputListView(LoginRequiredMixin, ListView):
    model = Output
    template_name = 'base/output_list.html'

    def get_queryset(self):
        object_list = Output.objects.all()
        query = self.request.GET.get('query')
        if query:
            if ' ' in query or '　' in query:
                queries = query.split()
                print(queries)
                for query in queries:
                    print(query)
                    object_list = object_list.filter(
                        Q(question__icontains=query) | Q(description__icontains=query)
                    )
            else:
                object_list = object_list.filter(
                    Q(question__icontains=query) | Q(description__icontains=query)
                )
        return object_list

class TagOutputListView(LoginRequiredMixin, ListView):
    model = Output
    template_name = 'base/output_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.tag = get_object_or_404(OutputTagModel, slug=slug)
        return super().get_queryset().filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class OutputCreateView(LoginRequiredMixin, CreateView):
    model = Output
    fields = (
        'question',
        'description',
    )
    template_name = 'base/output_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form)
        messages.success(self.request, 'アウトプットを作成しました')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('base:index')

class OutputDetailView(LoginRequiredMixin, DetailView):
    model = Output
    template_name = 'base/output_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output'] = Output.objects.get(pk=self.kwargs['pk'])
        return context