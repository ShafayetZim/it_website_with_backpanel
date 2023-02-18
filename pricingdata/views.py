from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def dashboard(request):
    context = {
        'nav_bar': "dashboard"
    }
    return render(request, 'index.html', context)


class BgPricingList(LoginRequiredMixin, ListView):
    model = BgPricing
    template_name = 'pricing/pricing_bg_list.html'
    context_object_name = 'pricing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pricing Bg List"
        context["nav_bar"] = "bg_pricing"
        context['pricing'] = self.model.objects.all().order_by('-id')
        return context


class BgPricingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BgPricing
    form_class = BgPricingCreateForm
    success_url = reverse_lazy('pricing-bg-list')
    template_name = 'pricing/pricing_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_pricing"
        return context


class PricingList(LoginRequiredMixin, ListView):
    model = Pricing
    template_name = 'pricing/pricing_list.html'
    context_object_name = 'pricing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pricing List"
        context["nav_bar"] = "pricing"
        context['pricing'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_pricing(request):
    template_name = 'pricing/pricing_new.html'

    if request.method == 'GET':
        print("GET called")
        pricing_form = PricingCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        pricing_form = PricingCreateForm(request.POST, request.FILES)

        if pricing_form.is_valid():
            pricing = pricing_form.save(commit=False)
            pricing.save()

            messages.add_message(request, messages.SUCCESS, 'New Pricing Entry Successful')
            return redirect('pricing-list')

        else:
            print("Not Valid Create Form")
            print(pricing_form.errors)

    return render(request, template_name, {
        'pricing_form': pricing_form,
        'title': 'New Pricing',
        'nav_bar': 'pricing',
    })


class PricingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pricing
    form_class = PricingCreateForm
    success_url = reverse_lazy('pricing-list')
    template_name = 'pricing/pricing_update.html'
    success_message = "Pricing was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pricing Blog Information"
        context["nav_bar"] = "pricing"
        return context


@login_required()
def pricing_delete(request, id):
    if request.method == 'GET':
        instance = Pricing.objects.get(id=id)
        Pricing.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('pricing-list')
