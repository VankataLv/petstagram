from django.urls import path, include

from petstagram.photos.views import add_photo, view_photo_details, edit_photo

urlpatterns = (
    path('add/', add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', view_photo_details, name='photo-details'),
        path('edit/', edit_photo, name='photo-edit'),
    ])),
)
