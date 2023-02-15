from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bg_portfolio', views.BgPortfolioList.as_view(), name="portfolio-bg-list"),
    path('update_portfolio_bg/<int:pk>', views.BgPortfolioUpdateView.as_view(), name='portfolio-bg-update'),
    path('portfolio_list', views.PortfolioList.as_view(), name="portfolio-list"),
    path('update_portfolio/<int:pk>', views.PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('portfolio', views.new_portfolio, name="portfolio"),
    path('delete_portfolio/<int:id>', views.portfolio_delete, name="delete-portfolio"),
    path('portfolio_detail_list', views.PortfolioDetailList.as_view(), name="portfolio-detail-list"),
    path('update_portfolio_detail/<int:pk>', views.PortfolioDetailUpdateView.as_view(), name='portfolio-detail-update'),
    path('portfolio_detail', views.new_portfolio_detail, name="portfolio-detail"),
    path('delete_portfolio_detail/<int:id>', views.details_delete, name="delete-portfolio-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
