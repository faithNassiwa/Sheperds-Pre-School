from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^about-us/letter/$', views.aboutUsLetter, name = 'about-us-letter'),
    url(r'^about-us/mvv/$', views.mvv, name = 'about-us-mvv'),
    url(r'^about-us/team/$', views.aboutUsTeam, name = 'about-us-team'),
    url(r'^about-us/board/$', views.aboutUsBoard, name = 'about-us-board'),
    url(r'^facilities/$', views.facilities, name = 'facilities'),
    url(r'^events/$', views.events, name = 'events'),
    url(r'^kids/gallery/$', views.students, name = 'students'),
    url(r'^kids/anthem/$', views.anthem, name = 'anthem'),
    url(r'^parents/$', views.parents, name = 'parents'),
    url(r'^parents/administration/$', views.administration, name = 'administration'),
    url(r'^parents/fees/$', views.fees, name = 'fees'),
    url(r'^contact-us/$', views.contactUs, name = 'contact-us'),
    url(r'^facilities/classes/$', views.classes, name = 'classes'),
    url(r'^facilities/tellyroom/$', views.tellyroom, name = 'tellyroom'),
    url(r'^facilities/playground/$', views.playgrounds, name = 'playground'),
    url(r'^facilities/kitchen/$', views.kitchen, name = 'kitchen'),
    url(r'^facilities/sickbay/$', views.sickbay, name = 'sickbay'),
    url(r'^facilities/washrooms/$', views.washrooms, name = 'washrooms'),
    
]
