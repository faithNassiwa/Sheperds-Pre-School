from django.conf.urls import url
from . import views
from .views import PreAdmissionCreate


urlpatterns = [
    url(r'^parents/application/pre_admission/$', views.PreAdmissionCreate.as_view(), name = 'admission'),
    url(r'^careers/$', views.CareerCreate.as_view(), name = 'careers'),
    url(r'^parents/application/pre_admission/thank-you/$', views.thanks, name='thanks'),
    url(r'^career/thank-you/$', views.thanksc, name='thanksc'),

    
]
