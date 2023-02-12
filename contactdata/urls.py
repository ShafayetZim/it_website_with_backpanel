from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bg_contact', views.BgContactList.as_view(), name="contact-bg-list"),
    path('update_contact_bg/<int:pk>', views.BgContactUpdateView.as_view(), name='contact-bg-update'),
    path('contact', views.ContactList.as_view(), name="contact-list"),
    path('update_contact/<int:pk>', views.ContactUpdateView.as_view(), name='contact-update'),
    path('phone', views.PhoneList.as_view(), name="phone-list"),
    path('update_phone/<int:pk>', views.PhoneUpdateView.as_view(), name='phone-update'),
    path('new_phone', views.new_phone, name="new-phone"),
    path('delete_phone/<int:id>', views.phone_delete, name="delete-phone"),
    path('email', views.EmailList.as_view(), name="email-list"),
    path('update_email/<int:pk>', views.EmailUpdateView.as_view(), name='email-update'),
    path('new_email', views.new_email, name="new-email"),
    path('delete_email/<int:id>', views.email_delete, name="delete-email"),
    path('office', views.OfficeList.as_view(), name="office-list"),
    path('update_office/<int:pk>', views.OfficeUpdateView.as_view(), name='office-update'),
    path('new_office', views.new_office, name="new-office"),
    path('delete_office/<int:id>', views.office_delete, name="delete-office"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
