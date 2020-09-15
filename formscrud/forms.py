from django import forms
from .models import Blog

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'user', 'content']
