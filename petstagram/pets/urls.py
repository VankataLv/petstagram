from django.urls import path, include

from petstagram.pets.views import AddPetView, PetDetailsView, \
    PetEditView, PetDeleteView

urlpatterns = (
    path('add/', AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailsView.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeleteView.as_view(), name='pet-delete'),
    ])),
)
