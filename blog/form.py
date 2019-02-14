from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
#모델을 기반으로 할 때는 ModelForm 임의라면 forms.Form
    class Meta:
        model = Blog
        fields = ['title', 'body']