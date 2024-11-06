from django.urls import path, include

from petstagram.pets.views import add_pet, show_pet_details, edit_pet, delete_pet

urlpatterns = (
    path('add/', add_pet, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', show_pet_details, name='pet-details'),
        path('edit/', edit_pet, name='pet-edit'),
        path('delete/', delete_pet, name='pet-delete'),
    ])),
)
