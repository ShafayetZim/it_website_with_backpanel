from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('all_user', views.user_list, name="all-users"),
    path('user_delete/<int:id>', views.user_delete, name="user-delete"),
    path('update_user/<int:pk>', views.UserUpdateView.as_view(), name='update_user'),
    path('users/<int:user_id>/permissions/', views.user_permissions, name='user_permissions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
