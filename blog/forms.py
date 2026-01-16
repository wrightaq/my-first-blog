# using to create a standard form for any new post
from django import forms

from .models import Post

class PostForm(forms.ModelForm): #forms.ModelForm makes is a Django form

    class Meta: # tells Django which model should be used to create the form
        model = Post
        fields = ('title', 'text') #narrow down which fields you want included from the model

