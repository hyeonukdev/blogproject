from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
#모델을 기반으로 할 때는 ModelForm 임의라면 forms.Form
    class Meta:
        model = Blog
        fields = ['title', 'body']

# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three'),('4','four')])