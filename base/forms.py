import sys
sys.dont_write_bytecode = True

from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, PlanReply

class UserCreationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('email',)
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name',
            'icon',
            'introduction',
            'target',
            'dream',
        )

class PlanReplyForm(forms.ModelForm):
    class Meta:
        model = PlanReply
        fields = (
            'entry',
            'party',
            'status',
            'desired',
            'question',
            'to_ayaka',
            'others',
        )