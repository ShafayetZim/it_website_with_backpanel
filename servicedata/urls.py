from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bg_service', views.BgServiceList.as_view(), name="service-bg-list"),
    path('update_service_bg/<int:pk>', views.BgServiceUpdateView.as_view(), name='service-bg-update'),
    path('service', views.ServiceList.as_view(), name="service-list"),
    path('update_service/<int:pk>', views.ServiceUpdateView.as_view(), name='service-update'),
    path('new_service', views.new_service, name="new-service"),
    path('delete_service/<int:id>', views.service_delete, name="delete-service"),
    path('progress', views.ProgressList.as_view(), name="progress-list"),
    path('update_progress/<int:pk>', views.ProgressUpdateView.as_view(), name='progress-update'),
    path('new_progress', views.new_progress, name="new-progress"),
    path('delete_progress/<int:id>', views.progress_delete, name="delete-progress"),
    path('experience_service', views.ExperienceList.as_view(), name="experience-service-list"),
    path('update_experience_service/<int:pk>', views.ExperienceUpdateView.as_view(), name='experience-service-update'),
    path('testimonial', views.TestimonialList.as_view(), name="testimonial-list"),
    path('update_testimonial/<int:pk>', views.TestimonialUpdateView.as_view(), name='testimonial-update'),
    path('new_testimonial', views.new_testimonial, name="new-testimonial"),
    path('delete_testimonial/<int:id>', views.testimonial_delete, name="delete-testimonial"),
    path('review', views.ReviewList.as_view(), name="review-list"),
    path('update_review/<int:pk>', views.ReviewUpdateView.as_view(), name='review-update'),
    path('new_review', views.new_review, name="new-review"),
    path('delete_review/<int:id>', views.review_delete, name="delete-review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
