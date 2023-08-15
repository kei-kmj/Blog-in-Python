from django.urls import path
from .views import blog_list
from .views import ReportListView, create_report, report_detail, edit_report, delete_report
from .views import UserListView, UserDetailView
from . import views

urlpatterns = [
    path('', blog_list, name='blog_list'),  # ブログ一覧画面
    path('report/', ReportListView.as_view(), name='report_list'),
    path('report/create/', create_report, name='create_report'),
    path('report/<int:report_id>/', report_detail, name='report_detail'),
    path('report/<int:report_id>/edit/', edit_report, name='edit_report'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),


]
