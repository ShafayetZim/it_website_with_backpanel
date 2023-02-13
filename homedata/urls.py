from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('slider', views.SliderList.as_view(), name="slider-list"),
    path('update_slider/<int:pk>', views.SliderUpdateView.as_view(), name='slider-update'),
    path('new_slider', views.new_slider, name="new-slider"),
    path('delete_slider/<int:id>', views.slider_delete, name="delete-slider"),
    path('service_home', views.ServiceList.as_view(), name="service-home-list"),
    path('update_service_home/<int:pk>', views.ServiceUpdateView.as_view(), name='service-home-update'),
    path('new_service_home', views.new_service, name="new-service-home"),
    path('delete_service_home/<int:id>', views.service_delete, name="delete-service-home"),
    path('project', views.ProjectList.as_view(), name="project-list"),
    path('update_project/<int:pk>', views.ProjectUpdateView.as_view(), name='project-update'),
    path('new_project', views.new_project, name="new-project"),
    path('delete_project/<int:id>', views.project_delete, name="delete-project"),
    path('experience_home', views.ExperienceList.as_view(), name="experience-home-list"),
    path('update_experience_home/<int:pk>', views.ExperienceUpdateView.as_view(), name='experience-home-update'),
    path('new_experience_home', views.new_experience, name="new-experience-home"),
    path('delete_experience_home/<int:id>', views.experience_delete, name="delete-experience-home"),
    path('about', views.AboutList.as_view(), name="about-list"),
    path('update_about/<int:pk>', views.AboutUpdateView.as_view(), name='about-update'),
    path('new_about', views.new_about, name="new-about"),
    path('delete_about/<int:id>', views.about_delete, name="delete-about"),
    path('speciality', views.SpecialityList.as_view(), name="speciality-list"),
    path('update_speciality/<int:pk>', views.SpecialityUpdateView.as_view(), name='speciality-update'),
    path('new_speciality', views.new_speciality, name="new-speciality"),
    path('delete_speciality/<int:id>', views.speciality_delete, name="delete-speciality"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
