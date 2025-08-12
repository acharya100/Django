from django import forms 
from myapp1.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']