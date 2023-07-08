from django import forms
from blogs.models import BlogPost
class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'title':'','text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
