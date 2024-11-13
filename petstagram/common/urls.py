from django.urls import path


from petstagram.common.views import like_functionality, copy_link_to_clipboard, add_comment, HomePage

urlpatterns = (
    path('', HomePage.as_view(), name='show-home-page'),
    path('like/<int:photo_id>', like_functionality, name='like'),
    path('share/<int:photo_id>', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', add_comment, name='comment'),
)