from django.urls import path
from .views import BlogListView, ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView, UserListView, UserDetailView, RegisterView, IndexRedirectView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # ブログ一覧画面
    path('report/', ReportListView.as_view(), name='report_list'),
    path('report/create/', ReportCreateView.as_view(), name='create_report'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('report/<int:pk>/edit/', ReportUpdateView.as_view(), name='edit_report'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name='delete_report'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),  # ユーザー登録
    path('index_redirect/', IndexRedirectView.as_view(), name='index_redirect'),  # インデックスリダイレクト


]
