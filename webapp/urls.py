from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home_page', views.home, name="home-page"),
    path('about_page', views.about, name="about-page"),
    path('pricing_page', views.pricing, name="pricing-page"),
    path('contact_page', views.contact, name="contact-page"),
    path('blog_page', views.blog, name="blog-page"),
    path('blog_detail_page', views.blog_detail, name="blog-detail-page"),
    path('portfolio_page', views.portfolio, name="portfolio-page"),
    path('portfolio_detail_page', views.portfolio_detail, name="portfolio-detail-page"),
    path('service_page', views.service, name="service-page"),
    path('service_detail_page', views.service_detail, name="service-detail-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
