from django import forms
from .models import *


class SkillFrom(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('category', 'title', 'time', 'description',)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20)


class SkillRateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rate',)
