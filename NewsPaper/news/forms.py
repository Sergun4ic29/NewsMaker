from django import forms
from .models import Post
from django.core.exceptions import ValidationError

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
#from .models import BaseRegistrForm

#class BaseRegisterView(CreateView):
    #model = User
    #form_class = BaseRegistrForm
    #success_url = '/news'



#class BaseRegistrForm(UserCreationForm):
    #name = forms.CharField(label='Имя')
    #email = forms.EmailField(label='email')
    #class Meta:
        #model = User
        #fields =(
            #'username',
            #'email'
        #)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'header',
            'text',
            'auther',
            'catygorys',
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

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm,self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user