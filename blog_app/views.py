from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, RedirectView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost
from .models import Report
from .models import UserProfile
from .forms import ReportForm
from .forms import BlogPostForm
from .forms import UserForm
from .forms import UserProfileForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class IndexRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('blog_list')
        else:
            return reverse_lazy('login')


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_app/blog_list.html'
    context_object_name = 'posts'


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog_app/create_blog_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_list')


class ReportListView(ListView):
    model = Report
    template_name = 'report/report_list.html'
    context_object_name = 'reports'


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'report/report_detail.html'
    context_object_name = 'report'


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'report/create_report.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('report_list')


class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'report/edit_report.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('report_detail', kwargs={'pk': self.object.pk})


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('report_list')

    def get(self, *args, **kwargs):  # Delete without confirmation
        return self.post(*args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'


class EditUserProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/edit_user_profile.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        return redirect('user_list')

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user

    # model = UserProfile
    # form_class = UserForm
    # second_form_class = UserProfileForm
    # template_name = 'user/edit_user_profile.html'
    # success_url = reverse_lazy('user_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_form'] = UserForm(instance=user)
        context['profileform'] = UserProfileForm(instance=user.userprofile)
        return context
        # context['form2'] = self.second_form_class(instance=self.request.user)
        # return context


    def form_valid(self, form):
        userform = UserForm(self.request.POST, instance=self.object)
        profileform = UserProfileForm(self.request.POST, instance=self.object.userprofile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(userform=userform, profileform=profileform))


