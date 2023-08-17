from django import forms
from .models import BlogPost
from .models import Report
from django.contrib.auth.models import User
from .models import UserProfile


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'body')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'report_date', 'content')
        widgets = {
            'report_date': forms.DateInput(attrs={'type': 'date'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    username = forms.CharField(
        required=True,
        error_messages={'required': '編集できません'}, )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname']
