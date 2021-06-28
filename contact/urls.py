from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('feedback/', views.CreateContact.as_view(), name='feedback'),
    path('about/', views.AboutView.as_view(), name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)