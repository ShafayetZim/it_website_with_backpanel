from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BgPortfolioList(LoginRequiredMixin, ListView):
    model = BgPortfolio
    template_name = 'portfolio/portfolio_bg_list.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Portfolio Bg List"
        context["nav_bar"] = "bg_portfolio"
        context['portfolio'] = self.model.objects.all().order_by('-id')
        return context


class BgPortfolioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BgPortfolio
    form_class = BgPortfolioForm
    success_url = reverse_lazy('portfolio-bg-list')
    template_name = 'portfolio/portfolio_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_portfolio"
        return context


class PortfolioList(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Portfolio List"
        context["nav_bar"] = "portfolio"
        context['portfolio'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_portfolio(request):
    template_name = 'portfolio/portfolio_new.html'

    if request.method == 'GET':
        print("GET called")
        portfolio_form = PortfolioForm(None)

    elif request.method == 'POST':
        print("Post called")
        portfolio_form = PortfolioForm(request.POST, request.FILES)

        if portfolio_form.is_valid():
            portfolio = portfolio_form.save(commit=False)
            portfolio.save()

            messages.add_message(request, messages.SUCCESS, 'New Portfolio Entry Successful')
            return redirect('portfolio-list')

        else:
            print("Not Valid Create Form")
            print(portfolio_form.errors)

    return render(request, template_name, {
        'portfolio_form': portfolio_form,
        'title': 'New Portfolio',
        'nav_bar': 'portfolio',
    })


class PortfolioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    success_url = reverse_lazy('portfolio-list')
    template_name = 'portfolio/portfolio_update.html'
    success_message = "Portfolio was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Portfolio Information"
        context["nav_bar"] = "portfolio"
        return context


@login_required()
def portfolio_delete(request, id):
    if request.method == 'GET':
        instance = Portfolio.objects.get(id=id)
        Portfolio.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('portfolio-list')


class PortfolioDetailList(LoginRequiredMixin, ListView):
    model = PortfolioDetails
    template_name = 'portfolio/portfolio_detail_list.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Portfolio Detail List"
        context["nav_bar"] = "portfolio_detail"
        context['portfolio'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_portfolio_detail(request):
    template_name = 'portfolio/portfolio_detail_new.html'

    if request.method == 'GET':
        print("GET called")
        detail_form = PortfolioDetailsForm(None)

    elif request.method == 'POST':
        print("Post called")
        detail_form = PortfolioDetailsForm(request.POST, request.FILES)

        if detail_form.is_valid():
            detail = detail_form.save(commit=False)
            detail.save()

            messages.add_message(request, messages.SUCCESS, 'New Detail Entry Successful')
            return redirect('portfolio-detail-list')

        else:
            print("Not Valid Create Form")
            print(detail_form.errors)

    return render(request, template_name, {
        'detail_form': detail_form,
        'title': 'New Portfolio Detail',
        'nav_bar': 'portfolio_detail',
    })


class PortfolioDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PortfolioDetails
    form_class = PortfolioDetailsForm
    success_url = reverse_lazy('portfolio-detail-list')
    template_name = 'portfolio/portfolio_detail_update.html'
    success_message = "Portfolio was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Portfolio Information"
        context["nav_bar"] = "portfolio_detail"
        return context


@login_required()
def details_delete(request, id):
    if request.method == 'GET':
        instance = PortfolioDetails.objects.get(id=id)
        PortfolioDetails.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('portfolio-detail-list')


@login_required()
def create_portfolio(request):
    if request.method == 'POST':
        portfolio_form = PortfolioForm(request.POST, request.FILES)
        portfolio_details_form = PortfolioDetailsForm(request.POST)

        if portfolio_form.is_valid() and portfolio_details_form.is_valid():
            portfolio = portfolio_form.save()
            portfolio_details = portfolio_details_form.save(commit=False)
            portfolio_details.code = portfolio
            portfolio_details.save()

            # success message and redirect
            return redirect('dashboard')

    else:
        portfolio_form = PortfolioForm()
        portfolio_details_form = PortfolioDetailsForm()

    return render(request, 'portfolio/portfolio_new.html', {'portfolio_form': portfolio_form, 'portfolio_details_form': portfolio_details_form})



