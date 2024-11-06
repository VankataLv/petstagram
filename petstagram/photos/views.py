from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('show-home-page')
    else:
        print("Form errors:", form.errors)  # Print form errors to debug
    context = {'form': form}

    return render(request, 'photos/photo-add-page.html', context)


def view_photo_details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk: int):
    Photo.objects.pet(pk=pk).delete()
    return redirect('show-home-page')