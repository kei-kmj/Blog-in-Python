from django.contrib import admin
from django.urls import path, include
from blog_app.views import IndexRedirectView, RegisterView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_list/', IndexRedirectView.as_view(), name='index_redirect'),
    path('register/', RegisterView.as_view(), name='register'),  # ユーザー登録
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('blog_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)