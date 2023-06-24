from django import forms
from app1.models import WriteSomething

class WriteSomethingForm(forms.ModelForm):
    class Meta:
        model = WriteSomething
        fields = ['title', 'content']
