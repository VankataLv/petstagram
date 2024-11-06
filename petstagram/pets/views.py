from django.shortcuts import render


def add_pet(request):
    context = {}

    return render(request, 'pets/pet-add-page.html', context)


def show_pet_details(request, username: str, pet_slug: str):

    context = {}

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username: str, pet_slug: str):
    context = {}

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username: str, pet_slug: str):
    context = {}

    return render(request, 'pets/pet-delete-page.html', context)