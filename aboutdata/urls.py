from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bg_about', views.BgAboutList.as_view(), name="about-bg-list"),
    path('update_about_bg/<int:pk>', views.BgAboutUpdateView.as_view(), name='about-bg-update'),
    path('bg_experience', views.BgExperienceList.as_view(), name="experience-bg-list"),
    path('update_experience_bg/<int:pk>', views.BgExperienceUpdateView.as_view(), name='experience-bg-update'),
    path('experience', views.ExperienceList.as_view(), name="experience-list"),
    path('update_experience/<int:pk>', views.ExperienceUpdateView.as_view(), name='experience-update'),
    path('company', views.CompanyList.as_view(), name="company-list"),
    path('update_company/<int:pk>', views.CompanyUpdateView.as_view(), name='company-update'),
    path('feature', views.FeatureList.as_view(), name="feature-list"),
    path('update_feature/<int:pk>', views.FeatureUpdateView.as_view(), name='feature-update'),
    path('new_feature', views.new_feature, name="new-feature"),
    path('delete_feature/<int:id>', views.feature_delete, name="delete-feature"),
    path('progressbar', views.ProgressbarList.as_view(), name="progressbar-list"),
    path('update_progressbar/<int:pk>', views.ProgressbarUpdateView.as_view(), name='progressbar-update'),
    path('new_progressbar', views.new_progressbar, name="new-progressbar"),
    path('delete_progressbar/<int:id>', views.progressbar_delete, name="delete-progressbar"),
    path('team', views.TeamList.as_view(), name="team-list"),
    path('update_team/<int:pk>', views.TeamUpdateView.as_view(), name='team-update'),
    path('new_team', views.new_team, name="new-team"),
    path('delete_team/<int:id>', views.team_delete, name="delete-team"),
    path('partner', views.PartnerList.as_view(), name="partner-list"),
    path('update_partner/<int:pk>', views.PartnerUpdateView.as_view(), name='partner-update'),
    path('new_partner', views.new_partner, name="new-partner"),
    path('delete_partner/<int:id>', views.partner_delete, name="delete-partner"),
    path('process', views.ProcessList.as_view(), name="process-list"),
    path('update_process/<int:pk>', views.ProcessUpdateView.as_view(), name='process-update'),
    path('new_process', views.new_process, name="new-process"),
    path('delete_process/<int:id>', views.process_delete, name="delete-process"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
