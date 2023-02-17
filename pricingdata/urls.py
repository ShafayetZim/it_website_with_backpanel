from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('bg_pricing', views.BgPricingList.as_view(), name="pricing-bg-list"),
    path('update_pricing_bg/<int:pk>', views.BgPricingUpdateView.as_view(), name='pricing-bg-update'),
    path('pricing', views.PricingList.as_view(), name="pricing-list"),
    path('update_pricing/<int:pk>', views.PricingUpdateView.as_view(), name='pricing-update'),
    path('new_pricing', views.new_pricing, name="new-pricing"),
    path('delete_pricing/<int:id>', views.pricing_delete, name="delete-pricing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
