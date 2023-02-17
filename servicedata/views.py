from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required


@login_required()
class BgServiceList(ListView):
    model = BgService
    template_name = 'service/service_bg_list.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Service Bg List"
        context["nav_bar"] = "bg_service"
        context['service'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
class BgServiceUpdateView(SuccessMessageMixin, UpdateView):
    model = BgService
    form_class = BgServiceForm
    success_url = reverse_lazy('service-bg-list')
    template_name = 'service/service_bg_update.html'
    success_message = "Bg was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Bg Information"
        context["nav_bar"] = "bg_service"
        return context


@login_required()
class ExperienceList(ListView):
    model = Experience
    template_name = 'service/experience_list.html'
    context_object_name = 'experience_service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Experience List"
        context["nav_bar"] = "experience_service"
        context['experience'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
class ExperienceUpdateView(SuccessMessageMixin, UpdateView):
    model = Experience
    form_class = Experience
    success_url = reverse_lazy('experience-list')
    template_name = 'experience/experience_update.html'
    success_message = "Experience was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Experience Information"
        context["nav_bar"] = "experience_service"
        return context


@login_required()
class ServiceList(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Service List"
        context["nav_bar"] = "service"
        context['service'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_service(request):
    template_name = 'service/service_new.html'

    if request.method == 'GET':
        print("GET called")
        service_form = ServiceForm(None)

    elif request.method == 'POST':
        print("Post called")
        service_form = ServiceForm(request.POST, request.FILES)

        if service_form.is_valid():
            service = service_form.save(commit=False)
            service.save()

            messages.add_message(request, messages.SUCCESS, 'New Service Entry Successful')
            return redirect('service-list')

        else:
            print("Not Valid Create Form")
            print(service_form.errors)

    return render(request, template_name, {
        'service_form': service_form,
        'title': 'New Service',
        'nav_bar': 'service',
    })


@login_required()
class ServiceUpdateView(SuccessMessageMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service-list')
    template_name = 'service/service_update.html'
    success_message = "Service was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Service Information"
        context["nav_bar"] = "service"
        return context


@login_required()
def service_delete(request, id):
    if request.method == 'GET':
        instance = Service.objects.get(id=id)
        Service.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('service-list')


@login_required()
class ProgressList(ListView):
    model = Progress
    template_name = 'service/progress_list.html'
    context_object_name = 'progress'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Progress List"
        context["nav_bar"] = "progress"
        context['progress'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_progress(request):
    template_name = 'service/progress_new.html'

    if request.method == 'GET':
        print("GET called")
        progress_form = ProgressForm(None)

    elif request.method == 'POST':
        print("Post called")
        progress_form = ProgressForm(request.POST, request.FILES)

        if progress_form.is_valid():
            progress = progress_form.save(commit=False)
            progress.save()

            messages.add_message(request, messages.SUCCESS, 'New Slider Entry Successful')
            return redirect('progress-list')

        else:
            print("Not Valid Create Form")
            print(progress_form.errors)

    return render(request, template_name, {
        'progress_form': progress_form,
        'title': 'New Progress',
        'nav_bar': 'progress',
    })


@login_required()
class ProgressUpdateView(SuccessMessageMixin, UpdateView):
    model = Progress
    form_class = ProgressForm
    success_url = reverse_lazy('progress-list')
    template_name = 'home/progress_update.html'
    success_message = "Progress was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Progress Information"
        context["nav_bar"] = "progress"
        return context


@login_required()
def progress_delete(request, id):
    if request.method == 'GET':
        instance = Progress.objects.get(id=id)
        Progress.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('progress-list')


@login_required()
class TestimonialList(ListView):
    model = Testimonial
    template_name = 'service/testimonial_list.html'
    context_object_name = 'testimonial'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Testimonial List"
        context["nav_bar"] = "testimonial"
        context['testimonial'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_testimonial(request):
    template_name = 'service/testimonial_new.html'

    if request.method == 'GET':
        print("GET called")
        testimonial_form = TestimonialForm(None)

    elif request.method == 'POST':
        print("Post called")
        testimonial_form = TestimonialForm(request.POST, request.FILES)

        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.save()

            messages.add_message(request, messages.SUCCESS, 'New Slider Entry Successful')
            return redirect('slider-list')

        else:
            print("Not Valid Create Form")
            print(testimonial_form.errors)

    return render(request, template_name, {
        'testimonial_form': testimonial_form,
        'title': 'New Testimonial',
        'nav_bar': 'testimonial',
    })


@login_required()
class TestimonialUpdateView(SuccessMessageMixin, UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    success_url = reverse_lazy('testimonial-list')
    template_name = 'service/testimonial_update.html'
    success_message = "Testimonial was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Testimonial Information"
        context["nav_bar"] = "testimonial"
        return context


@login_required()
def testimonial_delete(request, id):
    if request.method == 'GET':
        instance = Testimonial.objects.get(id=id)
        Testimonial.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('testimonial-list')


@login_required()
class ReviewList(ListView):
    model = Review
    template_name = 'service/review_list.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Review List"
        context["nav_bar"] = "review"
        context['review'] = self.model.objects.all().order_by('-id')
        return context


@login_required()
def new_review(request):
    template_name = 'service/review_new.html'

    if request.method == 'GET':
        print("GET called")
        review_form = ReviewForm(None)

    elif request.method == 'POST':
        print("Post called")
        review_form = ReviewForm(request.POST, request.FILES)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.save()

            messages.add_message(request, messages.SUCCESS, 'New Review Entry Successful')
            return redirect('review-list')

        else:
            print("Not Valid Create Form")
            print(review_form.errors)

    return render(request, template_name, {
        'review_form': review_form,
        'title': 'New Review',
        'nav_bar': 'review',
    })


@login_required()
class ReviewUpdateView(SuccessMessageMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('review-list')
    template_name = 'service/review_update.html'
    success_message = "Review was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Review Information"
        context["nav_bar"] = "review"
        return context


@login_required()
def review_delete(request, id):
    if request.method == 'GET':
        instance = Review.objects.get(id=id)
        Review.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('review-list')


