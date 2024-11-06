from django.shortcuts import render


def register(request):
    context = {

    }

    return render(request, 'accounts/register-page.html', context)


def login(request):
    context = {

    }

    return render(request, 'accounts/login-page.html', context)


def show_profile_details(request, pk: int):
    context = {

    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk: int):
    context = {

    }

    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request, pk: int):
    context = {

    }

    return render(request, 'accounts/profile-delete-page.html', context)
