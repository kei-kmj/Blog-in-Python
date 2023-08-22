from django.urls import path
from .views import RegisterView, IndexRedirectView, EditUserProfileView, UserDetailView, UserListView, \
    ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView, BlogListView,\
    MeetingListView, MeetingDetailView, MeetingCreateView, MeetingUpdateView, MeetingDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # ブログ一覧画面
    path('report/', ReportListView.as_view(), name='report_list'),
    path('report/create/', ReportCreateView.as_view(), name='create_report'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('report/<int:pk>/edit/', ReportUpdateView.as_view(), name='edit_report'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name='delete_report'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path ('user/<int:pk>/edit/', EditUserProfileView.as_view(), name='edit_user_profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('index_redirect/', IndexRedirectView.as_view(), name='index_redirect'),
    path('meeting/', MeetingListView.as_view(), name='meeting_list'),
    path('meeting/<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),
    path('meeting/create/', MeetingCreateView.as_view(), name='create_meeting'),
    path('meeting/<int:pk>/edit/', MeetingUpdateView.as_view(), name='edit_meeting'),
    path('meeting/<int:pk>/delete/', MeetingDeleteView.as_view(), name='delete_meeting'),



]
