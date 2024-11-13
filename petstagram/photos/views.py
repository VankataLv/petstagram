from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('show-home-page')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user

        # photo.save()
        # form._save_m2m()
        return super().form_valid(form)

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


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()
        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()

        return context

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


class PhotoEditView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse_lazy(
            'photo-details',
            kwargs={'pk': self.object.pk ,},
        )

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