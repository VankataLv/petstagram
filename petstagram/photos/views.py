from django.shortcuts import render


def add_photo(request):
    context = {}

    return render(request, 'photos/photo-add-page.html', context)


def view_photo_details(request, pk: int):
    context = {}

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk: int):
    context = {}

    return render(request, 'photos/photo-edit-page.html', context)