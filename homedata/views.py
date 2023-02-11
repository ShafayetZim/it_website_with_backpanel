from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView


class SliderList(ListView):
    model = Slider
    template_name = 'home/slider_list.html'
    context_object_name = 'slider'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Slider List"
        context["nav_bar"] = "slider"
        context['slider'] = self.model.objects.all().order_by('-id')
        return context


def new_slider(request):
    template_name = 'home/slider_new.html'

    if request.method == 'GET':
        print("GET called")
        slider_form = SliderForm(None)

    elif request.method == 'POST':
        print("Post called")
        slider_form = SliderForm(request.POST, request.FILES)

        if slider_form.is_valid():
            slider = slider_form.save(commit=False)
            slider.save()

            messages.add_message(request, messages.SUCCESS, 'New Slider Entry Successful')
            return redirect('slider-list')

        else:
            print("Not Valid Create Form")
            print(slider_form.errors)

    return render(request, template_name, {
        'slider_form': slider_form,
        'title': 'New Slider',
        'nav_bar': 'slider',
    })


class SliderUpdateView(SuccessMessageMixin, UpdateView):
    model = Slider
    form_class = SliderForm
    success_url = reverse_lazy('slider-list')
    template_name = 'home/slider_update.html'
    success_message = "Slider was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Slider Information"
        context["nav_bar"] = "slider"
        return context


def slider_delete(request, id):
    if request.method == 'GET':
        instance = Slider.objects.get(id=id)
        Slider.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('slider-list')


class ServiceList(ListView):
    model = Service
    template_name = 'home/service_list.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Service List"
        context["nav_bar"] = "service"
        context['service'] = self.model.objects.all().order_by('-id')
        return context


def new_service(request):
    template_name = 'home/service_new.html'

    if request.method == 'GET':
        print("GET called")
        service_form = ServiceForm(None)

    elif request.method == 'POST':
        print("Post called")
        service_form = ServiceForm(request.POST, request.FILES)

        if service_form.is_valid():
            service = service_form.save(commit=False)
            service.save()

            messages.add_message(request, messages.SUCCESS, 'New Slider Entry Successful')
            return redirect('service-list')

        else:
            print("Not Valid Create Form")
            print(service_form.errors)

    return render(request, template_name, {
        'service_form': service_form,
        'title': 'New Service',
        'nav_bar': 'service',
    })


class ServiceUpdateView(SuccessMessageMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service-list')
    template_name = 'home/service_update.html'
    success_message = "Service was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Service Information"
        context["nav_bar"] = "service"
        return context


def service_delete(request, id):
    if request.method == 'GET':
        instance = Service.objects.get(id=id)
        Service.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('service-list')


class ProjectList(ListView):
    model = Project
    template_name = 'home/project_list.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project List"
        context["nav_bar"] = "project"
        context['project'] = self.model.objects.all().order_by('-id')
        return context


def new_project(request):
    template_name = 'home/project_new.html'

    if request.method == 'GET':
        print("GET called")
        project_form = ProjectForm(None)

    elif request.method == 'POST':
        print("Post called")
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.save()

            messages.add_message(request, messages.SUCCESS, 'New Project Entry Successful')
            return redirect('project-list')

        else:
            print("Not Valid Create Form")
            print(project_form.errors)

    return render(request, template_name, {
        'project_form': project_form,
        'title': 'New Project',
        'nav_bar': 'project',
    })


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')
    template_name = 'home/project_update.html'
    success_message = "Project was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Project Information"
        context["nav_bar"] = "project"
        return context


def project_delete(request, id):
    if request.method == 'GET':
        instance = Project.objects.get(id=id)
        Project.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('project-list')


class ExperienceList(ListView):
    model = Experience
    template_name = 'home/experience_list.html'
    context_object_name = 'experience'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Experience List"
        context["nav_bar"] = "experience"
        context['experience'] = self.model.objects.all().order_by('-id')
        return context


def new_experience(request):
    template_name = 'home/experience_new.html'

    if request.method == 'GET':
        print("GET called")
        experience_form = ExperienceForm(None)

    elif request.method == 'POST':
        print("Post called")
        experience_form = ExperienceForm(request.POST, request.FILES)

        if experience_form.is_valid():
            experience = experience_form.save(commit=False)
            experience.save()

            messages.add_message(request, messages.SUCCESS, 'New Experience Entry Successful')
            return redirect('experience-list')

        else:
            print("Not Valid Create Form")
            print(experience_form.errors)

    return render(request, template_name, {
        'experience_form': experience_form,
        'title': 'New Experience',
        'nav_bar': 'experience',
    })


class ExperienceUpdateView(SuccessMessageMixin, UpdateView):
    model = Experience
    form_class = ExperienceForm
    success_url = reverse_lazy('experience-list')
    template_name = 'home/experience_update.html'
    success_message = "Experience was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Experience Information"
        context["nav_bar"] = "experience"
        return context


def experience_delete(request, id):
    if request.method == 'GET':
        instance = Experience.objects.get(id=id)
        Experience.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('experience-list')


class AboutList(ListView):
    model = About
    template_name = 'home/about_list.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About List"
        context["nav_bar"] = "about"
        context['About'] = self.model.objects.all().order_by('-id')
        return context


def new_about(request):
    template_name = 'home/about_new.html'

    if request.method == 'GET':
        print("GET called")
        about_form = AboutForm(None)

    elif request.method == 'POST':
        print("Post called")
        about_form = AboutForm(request.POST, request.FILES)

        if about_form.is_valid():
            about = about_form.save(commit=False)
            about.save()

            messages.add_message(request, messages.SUCCESS, 'New About Entry Successful')
            return redirect('about-list')

        else:
            print("Not Valid Create Form")
            print(about_form.errors)

    return render(request, template_name, {
        'about_form': about_form,
        'title': 'New About',
        'nav_bar': 'about',
    })


class AboutUpdateView(SuccessMessageMixin, UpdateView):
    model = About
    form_class = AboutForm
    success_url = reverse_lazy('about-list')
    template_name = 'home/about_update.html'
    success_message = "About was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update About Information"
        context["nav_bar"] = "about"
        return context


def about_delete(request, id):
    if request.method == 'GET':
        instance = About.objects.get(id=id)
        About.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('about-list')


class SpecialityList(ListView):
    model = Speciality
    template_name = 'home/speciality_list.html'
    context_object_name = 'speciality'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Speciality List"
        context["nav_bar"] = "speciality"
        context['speciality'] = self.model.objects.all().order_by('-id')
        return context


def new_speciality(request):
    template_name = 'home/speciality_new.html'

    if request.method == 'GET':
        print("GET called")
        speciality_form = SpecialityForm(None)

    elif request.method == 'POST':
        print("Post called")
        speciality_form = SpecialityForm(request.POST, request.FILES)

        if speciality_form.is_valid():
            speciality = speciality_form.save(commit=False)
            speciality.save()

            messages.add_message(request, messages.SUCCESS, 'New Speciality Entry Successful')
            return redirect('speciality-list')

        else:
            print("Not Valid Create Form")
            print(speciality_form.errors)

    return render(request, template_name, {
        'speciality_form': speciality_form,
        'title': 'New Speciality',
        'nav_bar': 'speciality',
    })


class SpecialityUpdateView(SuccessMessageMixin, UpdateView):
    model = Speciality
    form_class = SpecialityForm
    success_url = reverse_lazy('speciality-list')
    template_name = 'home/speciality_update.html'
    success_message = "Speciality was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Speciality Information"
        context["nav_bar"] = "speciality"
        return context


def speciality_delete(request, id):
    if request.method == 'GET':
        instance = Speciality.objects.get(id=id)
        Speciality.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('speciality-list')
