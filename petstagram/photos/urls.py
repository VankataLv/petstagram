from django.urls import path, include


from petstagram.photos.views import delete_photo, AddPhotoView, \
    PhotoEditView, PhotoDetailsView

urlpatterns = (
    path('add/', AddPhotoView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', PhotoEditView.as_view(), name='photo-edit'),
        path('delete/', delete_photo, name='photo-delete'),
    ])),
)
