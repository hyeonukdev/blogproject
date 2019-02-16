from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
#모델을 기반으로 할 때는 ModelForm 임의라면 forms.Form
    class Meta:
        model = Blog
        fields = ['title', 'body']

# class BlogPost(forms.Form):
#     title = forms.CharField(max_length=30)
#     body = forms.CharField()  
#     age = forms.IntegerField()
#     files = forms.FileField()