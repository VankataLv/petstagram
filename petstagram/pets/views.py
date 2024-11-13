from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    # queryset = Pet.objects.all()
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1,})

def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form,}

    return render(request, 'pets/pet-add-page.html', context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['pet'].photo_set.all()
        context['comment_form'] = CommentForm()
        return context


def show_pet_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


class PetEditView(UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetForm

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )

def edit_pet(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {'form': form}

    return render(request, 'pets/pet-edit-page.html', context)


class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

def delete_pet(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, 'pets/pet-delete-page.html', context)
