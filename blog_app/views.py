from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost
from .models import Report
from .forms import ReportForm
from .forms import BlogPostForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            form.save()
            # Redirect to the login page
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def index_redirect(request):
    if request.user.is_authenticated:
        return redirect('blog_list')
    else:
        return redirect('login')


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_app/blog_list.html', {'posts': posts})


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_app/create_blog_post.html', {'form': form})


class ReportListView(ListView):
    model = Report
    template_name = 'report/report_list.html'
    context_object_name = 'reports'


@login_required
def report_detail(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, 'report/report_detail.html', {'report': report})


@login_required
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report/create_report.html', {'form': form})


@login_required
def edit_report(request, report_id):
    report = Report.objects.get(id=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.save()
            return redirect('report_detail', report_id=report.id)
    else:
        form = ReportForm(instance=report)
    return render(request, 'report/edit_report.html', {'form': form})


@login_required
def delete_report(request, report_id):
    Report.objects.get(id=report_id).delete()
    return redirect('report_list')


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'
