from django.urls import path
from index import views


urlpatterns=[
    path('',views.index,name='index'),
    path('company/',views.company,name='company'),
    path('meet_the_team/',views.meet_the_team,name="meet_the_team"),
    path('privacy_policy/',views.privacy_policy,name="privacy_policy"),
    path('contact/',views.contact,name='contact'),
    path('work/',views.work,name='work'),
    path('services/',views.services,name='services'),
    path('service/<service_slug>/',views.service,name="service"),
    path('run_script/',views.run_service_script),

]
