from django import forms
from .models import Blog
from .models import UploadFileModel

class BlogPost(forms.ModelForm):
# 모델을 기반으로 할 때는 ModelForm 임의라면 forms.Form
    class Meta:
        model = Blog
        fields = ['title', 'body']

# class BlogPost(forms.Form):
#     title = forms.CharField(max_length=30)
#     body = forms.CharField()  
#     files = forms.FileField()


class PicPost(forms.Form):
    title = forms.CharField(max_length=30)
    body = forms.CharField()  
    files = forms.FileField()


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False