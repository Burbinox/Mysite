from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('doswiadczenie', views.doswiadczenie, name='doswiadczenie'),
    path('hobby', views.hobby, name='hobby'),
    path('umiejetnosci', views.umiejetnosci, name='umiejetnosci'),
    path('strona_glowna', views.strona_glowna, name='strona_glowna')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
