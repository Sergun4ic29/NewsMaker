from django import forms
from .models import Post
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'header',
            'text',
            'auther',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if text is not None and len(text) > 250 and len(text) < 10:
            raise ValidationError({'text':'Slishkom dlinno'})
        header = cleaned_data.get('header')
        if len(header) < 5:
            raise ValidationError('O4en korotkii zagolovok')
        return cleaned_data

