from django.contrib.auth.views import LogoutView
from django.urls import path, include

from petstagram.accounts.views import show_profile_details, edit_profile, delete_profile, AppUserRegisterView, \
    AppUserLoginView

urlpatterns = (
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='profile-details'),
        path('edit/', edit_profile, name='profile-edit'),
        path('delete/', delete_profile, name='profile-delete'),
    ])),
)