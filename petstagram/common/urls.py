from django.urls import path

from petstagram.common.views import show_home_page, like_functionality, copy_link_to_clipboard, add_comment

urlpatterns = (
    path('', show_home_page, name='show-home-page'),
    path('like/<int:photo_id>', like_functionality, name='like'),
    path('share/<int:photo_id>', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', add_comment, name='comment'),
)