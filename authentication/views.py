from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from authentication import models, forms
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User, Permission


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': "Edit Profile",
        'nav_bar': "profile"
    }
    return render(request, 'authentication/profile.html', context)


@login_required()
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Account has been created! S/He Can login now.')
            return redirect('all-users')

    else:
        form = forms.UserRegisterForm()

    context = {
        'form': form,
        'title': 'New User',
        'nav_bar': 'new_user',
    }
    return render(request, 'authentication/register.html', context)


@login_required()
def user_list(request):
    items = models.User.objects.filter(is_superuser=False).all().order_by('-id')
    context = {
        'items': items,
        'title': 'User List',
        'nav_bar': 'user_list',
    }
    return render(request, 'authentication/user_list.html', context)


@login_required()
def user_delete(request, id):
    if request.method == 'GET':
        instance = models.User.objects.get(id=id)
        models.User.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success. User has been deleted.')
        return redirect('all-users')


class UserUpdateView(UpdateView):
    model = models.User
    form_class = forms.UpdateUser
    success_url = reverse_lazy('all-users')
    template_name = 'authentication/update_user.html'
    success_message = "User was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Information"
        context["nav_bar"] = "user_list"
        return context


def user_permissions(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        # Get list of selected permission IDs from form submission
        selected_permissions = request.POST.getlist('permissions')

        # Update user permissions
        user.user_permissions.set(selected_permissions)
        user.save()

        # Redirect to user permissions page
        return redirect('user_permissions', user_id=user_id)

    user_permissions = user.user_permissions.all()
    all_permissions = Permission.objects.all()
    context = {
        'user': user,
        'user_permissions': user_permissions,
        'all_permissions': all_permissions,
    }
    return render(request, 'authentication/user_permissions.html', context)


