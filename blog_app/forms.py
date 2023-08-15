from django import forms
from .models import BlogPost
from .models import Report


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'body')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'content')
