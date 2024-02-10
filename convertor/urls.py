from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('jpgtopdf', views.jpgToPdf),
    path('pdftojpg', views.pdftojpg),
    path('pdftableextract', views.pdftableextract),
    path('pdf_view', views.pdf_view)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)