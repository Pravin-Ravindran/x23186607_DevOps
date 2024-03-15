from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home,name='Home'),
    path('about/',views.about,name='About'),
    path('checkout/',views.checkout,name='Checkout'),
    path('confirmation/',views.confirmation,name='Confirm'),
    path('contactus/',views.contactus,name='Contact'),
    ]
    
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
