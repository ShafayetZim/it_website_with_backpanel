from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BgContactList(LoginRequiredMixin, ListView):
    model = ContactBg
    template_name = 'contact/contact_bg_list.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Bg List"
        context["nav_bar"] = "bg_contact"
        context['contact'] = self.model.objects.all().order_by('-id')
        return context


class BgContactUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ContactBg
    form_class = ContactBgForm
    success_url = reverse_lazy('contact-bg-list')
    template_name = 'contact/contact_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_contact"
        return context


class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact List"
        context["nav_bar"] = "contact"
        context['contact'] = self.model.objects.all().order_by('-id')
        return context


# not necessary
def new_contact(request):
    template_name = 'contact/contact_new.html'

    if request.method == 'GET':
        print("GET called")
        contact_form = ContactForm(None)

    elif request.method == 'POST':
        print("Post called")
        contact_form = ContactForm(request.POST, request.FILES)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            messages.add_message(request, messages.SUCCESS, 'New Contact Entry Successful')
            return redirect('contact-list')

        else:
            print("Not Valid Create Form")
            print(contact_form.errors)

    return render(request, template_name, {
        'contact_form': contact_form,
        'title': 'New Contact',
        'nav_bar': 'contact',
    })


class ContactUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact-list')
    template_name = 'contact/contact_update.html'
    success_message = "Contact was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Blog Information"
        context["nav_bar"] = "contact"
        return context


# not necessary
def contact_delete(request, id):
    if request.method == 'GET':
        instance = Contact.objects.get(id=id)
        Contact.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('contact-list')


class PhoneList(LoginRequiredMixin, ListView):
    model = Phone
    template_name = 'contact/phone_list.html'
    context_object_name = 'phone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Phone List"
        context["nav_bar"] = "phone"
        context['phone'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_phone(request):
    template_name = 'contact/phone_new.html'

    if request.method == 'GET':
        print("GET called")
        phone_form = PhoneForm(None)

    elif request.method == 'POST':
        print("Post called")
        phone_form = PhoneForm(request.POST, request.FILES)

        if phone_form.is_valid():
            phone = phone_form.save(commit=False)
            phone.save()

            messages.add_message(request, messages.SUCCESS, 'New Phone Entry Successful')
            return redirect('phone-list')

        else:
            print("Not Valid Create Form")
            print(phone_form.errors)

    return render(request, template_name, {
        'phone_form': phone_form,
        'title': 'New Phone',
        'nav_bar': 'phone',
    })


class PhoneUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy('phone-list')
    template_name = 'contact/phone_update.html'
    success_message = "Phone was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Phone Information"
        context["nav_bar"] = "phone"
        return context


@login_required()
def phone_delete(request, id):
    if request.method == 'GET':
        instance = Phone.objects.get(id=id)
        Phone.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('phone-list')


class EmailList(LoginRequiredMixin, ListView):
    model = Email
    template_name = 'contact/email_list.html'
    context_object_name = 'email'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Email List"
        context["nav_bar"] = "email"
        context['email'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_email(request):
    template_name = 'contact/email_new.html'

    if request.method == 'GET':
        print("GET called")
        email_form = EmailForm(None)

    elif request.method == 'POST':
        print("Post called")
        email_form = EmailForm(request.POST, request.FILES)

        if email_form.is_valid():
            email = email_form.save(commit=False)
            email.save()

            messages.add_message(request, messages.SUCCESS, 'New Email Entry Successful')
            return redirect('email-list')

        else:
            print("Not Valid Create Form")
            print(email_form.errors)

    return render(request, template_name, {
        'email_form': email_form,
        'title': 'New Email',
        'nav_bar': 'email',
    })


class EmailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('email-list')
    template_name = 'contact/email_update.html'
    success_message = "Email was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Email Information"
        context["nav_bar"] = "email"
        return context


@login_required()
def email_delete(request, id):
    if request.method == 'GET':
        instance = Email.objects.get(id=id)
        Email.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('email-list')


class OfficeList(LoginRequiredMixin, ListView):
    model = Office
    template_name = 'contact/office_list.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Office List"
        context["nav_bar"] = "office"
        context['office'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_office(request):
    template_name = 'contact/office_new.html'

    if request.method == 'GET':
        print("GET called")
        office_form = OfficeForm(None)

    elif request.method == 'POST':
        print("Post called")
        office_form = OfficeForm(request.POST, request.FILES)

        if office_form.is_valid():
            office = office_form.save(commit=False)
            office.save()

            messages.add_message(request, messages.SUCCESS, 'New Office Entry Successful')
            return redirect('office-list')

        else:
            print("Not Valid Create Form")
            print(office_form.errors)

    return render(request, template_name, {
        'office_form': office_form,
        'title': 'New Office',
        'nav_bar': 'office',
    })


class OfficeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Office
    form_class = OfficeForm
    success_url = reverse_lazy('office-list')
    template_name = 'contact/office_update.html'
    success_message = "Office was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Office Information"
        context["nav_bar"] = "office"
        return context


@login_required()
def office_delete(request, id):
    if request.method == 'GET':
        instance = Office.objects.get(id=id)
        Office.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('office-list')
