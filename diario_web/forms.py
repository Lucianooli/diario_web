from django import forms
from .models import Topic,Entry
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TopicForm(forms.ModelForm):
    class Meta:
            model = Topic
            fields = ['text']
            labels = {'text': ''}   


class EntryForm(forms.ModelForm):
      class Meta:
            model = Entry
            fields = ['text']
            labels = {'text': ''}
            widgets = {'text': forms.Textarea(attrs={'cols':80})}

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nome", max_length=254)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
        }
        help_texts = {
            'username': 'nome do usuario',
            'password1': None,
            'password2': None,
        }