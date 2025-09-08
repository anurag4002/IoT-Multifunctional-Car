from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Admin modifyng
admin.site.site_header = 'Multifunctional Car'
admin.site.site_title = 'Multifunctional Car'
admin.site.index_title = 'Welcome to Multifunctional Car Administration'

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('parts/', views.parts, name='parts'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('bts/', views.bts, name='bts'),
    path('partsV/', views.partsView, name='partsV'),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)