from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView


class BgAboutList(ListView):
    model = BgAbout
    template_name = 'about/about_bg_list.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Bg List"
        context["nav_bar"] = "bg_about"
        context['about'] = self.model.objects.all().order_by('-id')
        return context


# not necessary
def new_bg_about(request):
    template_name = 'about/about_bg_new.html'

    if request.method == 'GET':
        print("GET called")
        bg_form = BgAboutForm(None)

    elif request.method == 'POST':
        print("Post called")
        bg_form = BgAboutForm(request.POST, request.FILES)

        if bg_form.is_valid():
            bg = bg_form.save(commit=False)
            bg.save()

            messages.add_message(request, messages.SUCCESS, 'New Bg Entry Successful')
            return redirect('about-bg-list')

        else:
            print("Not Valid Create Form")
            print(bg_form.errors)

    return render(request, template_name, {
        'bg_form': bg_form,
        'title': 'New Bg About',
        'nav_bar': 'bg_about',
    })


class BgAboutUpdateView(SuccessMessageMixin, UpdateView):
    model = BgAbout
    form_class = BgAboutForm
    success_url = reverse_lazy('about-bg-list')
    template_name = 'about/about_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_about"
        return context


# not necessary
def bg_about_delete(request, id):
    if request.method == 'GET':
        instance = BgAbout.objects.get(id=id)
        BgAbout.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('about-bg-list')


class CompanyList(ListView):
    model = Company
    template_name = 'about/company_list.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Company List"
        context["nav_bar"] = "company"
        context['company'] = self.model.objects.all().order_by('-id')
        return context


class CompanyUpdateView(SuccessMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list')
    template_name = 'about/company_update.html'
    success_message = "Info was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "company"
        return context


class FeatureList(ListView):
    model = Feature
    template_name = 'about/feature_list.html'
    context_object_name = 'feature'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Feature List"
        context["nav_bar"] = "feature"
        context['feature'] = self.model.objects.all().order_by('-id')
        return context


def new_feature(request):
    template_name = 'about/feature_new.html'

    if request.method == 'GET':
        print("GET called")
        feature_form = FeatureForm(None)

    elif request.method == 'POST':
        print("Post called")
        feature_form = FeatureForm(request.POST)

        if feature_form.is_valid():
            feature = feature_form.save(commit=False)
            feature.save()

            messages.add_message(request, messages.SUCCESS, 'New Entry Successful')
            return redirect('feature-list')

        else:
            print("Not Valid Create Form")
            print(feature_form.errors)

    return render(request, template_name, {
        'feature_form': feature_form,
        'title': 'New Feature',
        'nav_bar': 'feature',
    })


class FeatureUpdateView(SuccessMessageMixin, UpdateView):
    model = Feature
    form_class = FeatureForm
    success_url = reverse_lazy('feature-list')
    template_name = 'about/feature_update.html'
    success_message = "Feature was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "feature"
        return context


def feature_delete(request, id):
    if request.method == 'GET':
        instance = Feature.objects.get(id=id)
        Feature.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('feature-list')


class ProgressbarList(ListView):
    model = Progressbar
    template_name = 'about/progressbar_list.html'
    context_object_name = 'progressbar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Progressbar List"
        context["nav_bar"] = "progressbar"
        context['progressbar'] = self.model.objects.all().order_by('-id')
        return context


def new_progressbar(request):
    template_name = 'about/progressbar_new.html'

    if request.method == 'GET':
        print("GET called")
        progressbar_form = ProgressbarForm(None)

    elif request.method == 'POST':
        print("Post called")
        progressbar_form = ProgressbarForm(request.POST)

        if progressbar_form.is_valid():
            progressbar = progressbar_form.save(commit=False)
            progressbar.save()

            messages.add_message(request, messages.SUCCESS, 'New Entry Successful')
            return redirect('progressbar-list')

        else:
            print("Not Valid Create Form")
            print(progressbar_form.errors)

    return render(request, template_name, {
        'progressbar_form': progressbar_form,
        'title': 'New Progressbar',
        'nav_bar': 'progressbar',
    })


class ProgressbarUpdateView(SuccessMessageMixin, UpdateView):
    model = Progressbar
    form_class = ProgressbarForm
    success_url = reverse_lazy('progressbar-list')
    template_name = 'about/progressbar_update.html'
    success_message = "Progressbar was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "progressbar"
        return context


def progressbar_delete(request, id):
    if request.method == 'GET':
        instance = Progressbar.objects.get(id=id)
        Progressbar.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('progressbar-list')


class BgExperienceList(ListView):
    model = ExperienceBg
    template_name = 'about/experience_bg_list.html'
    context_object_name = 'experience'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Experience Bg List"
        context["nav_bar"] = "bg_experience"
        context['experience'] = self.model.objects.all().order_by('-id')
        return context


class BgExperienceUpdateView(SuccessMessageMixin, UpdateView):
    model = ExperienceBg
    form_class = ExperienceBg
    success_url = reverse_lazy('experience-bg-list')
    template_name = 'about/experience_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_experience"
        return context


class ExperienceList(ListView):
    model = Experience
    template_name = 'about/experience_list.html'
    context_object_name = 'experience'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Experience List"
        context["nav_bar"] = "experience"
        context['experience'] = self.model.objects.all().order_by('-id')
        return context


class ExperienceUpdateView(SuccessMessageMixin, UpdateView):
    model = ExperienceBg
    form_class = ExperienceBg
    success_url = reverse_lazy('experience-list')
    template_name = 'about/experience_update.html'
    success_message = "Experience was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "experience"
        return context


class ProcessList(ListView):
    model = Process
    template_name = 'about/process_list.html'
    context_object_name = 'process'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Process List"
        context["nav_bar"] = "process"
        context['process'] = self.model.objects.all().order_by('-id')
        return context


def new_process(request):
    template_name = 'about/process_new.html'

    if request.method == 'GET':
        print("GET called")
        process_form = ProcessForm(None)

    elif request.method == 'POST':
        print("Post called")
        process_form = ProcessForm(request.POST)

        if process_form.is_valid():
            process = process_form.save(commit=False)
            process.save()

            messages.add_message(request, messages.SUCCESS, 'New Entry Successful')
            return redirect('process-list')

        else:
            print("Not Valid Create Form")
            print(process_form.errors)

    return render(request, template_name, {
        'process_form': process_form,
        'title': 'New Process',
        'nav_bar': 'process',
    })


class ProcessUpdateView(SuccessMessageMixin, UpdateView):
    model = Process
    form_class = ProcessForm
    success_url = reverse_lazy('process-list')
    template_name = 'about/process_update.html'
    success_message = "Process was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "process"
        return context


def process_delete(request, id):
    if request.method == 'GET':
        instance = Process.objects.get(id=id)
        Process.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('process-list')


class TeamList(ListView):
    model = Team
    template_name = 'about/team_list.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Team List"
        context["nav_bar"] = "team"
        context['team'] = self.model.objects.all().order_by('-id')
        return context


def new_team(request):
    template_name = 'about/team_new.html'

    if request.method == 'GET':
        print("GET called")
        team_form = TeamForm(None)

    elif request.method == 'POST':
        print("Post called")
        team_form = TeamForm(request.POST)

        if team_form.is_valid():
            team = team_form.save(commit=False)
            team.save()

            messages.add_message(request, messages.SUCCESS, 'New Entry Successful')
            return redirect('team-list')

        else:
            print("Not Valid Create Form")
            print(team_form.errors)

    return render(request, template_name, {
        'team_form': team_form,
        'title': 'New Team',
        'nav_bar': 'team',
    })


class TeamUpdateView(SuccessMessageMixin, UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('team-list')
    template_name = 'about/team_update.html'
    success_message = "Team was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "Team"
        return context


def team_delete(request, id):
    if request.method == 'GET':
        instance = Team.objects.get(id=id)
        Team.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('team-list')


class PartnerList(ListView):
    model = Partner
    template_name = 'about/partner_list.html'
    context_object_name = 'partner'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Partner List"
        context["nav_bar"] = "partner"
        context['partner'] = self.model.objects.all().order_by('-id')
        return context


def new_partner(request):
    template_name = 'about/partner_new.html'

    if request.method == 'GET':
        print("GET called")
        partner_form = PartnerForm(None)

    elif request.method == 'POST':
        print("Post called")
        partner_form = PartnerForm(request.POST)

        if partner_form.is_valid():
            partner = partner_form.save(commit=False)
            partner.save()

            messages.add_message(request, messages.SUCCESS, 'New Entry Successful')
            return redirect('partner-list')

        else:
            print("Not Valid Create Form")
            print(partner_form.errors)

    return render(request, template_name, {
        'partner_form': partner_form,
        'title': 'New Partner',
        'nav_bar': 'partner',
    })


class PartnerUpdateView(SuccessMessageMixin, UpdateView):
    model = Partner
    form_class = PartnerForm
    success_url = reverse_lazy('partner-list')
    template_name = 'about/partner_update.html'
    success_message = "Partner was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Information"
        context["nav_bar"] = "partner"
        return context


def partner_delete(request, id):
    if request.method == 'GET':
        instance = Progressbar.objects.get(id=id)
        Progressbar.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('partner-list')
