from django import forms
from app1.models import WriteSomething
from django.core.validators import FileExtensionValidator


class WriteSomethingForm(forms.ModelForm):
    image = forms.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    class Meta:
        model = WriteSomething
        fields = ['title', 'content', 'image']
