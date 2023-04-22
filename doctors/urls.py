from django.contrib import admin
from django.urls import path,include
from .views import doctor_viewset , Appointment_viewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'doctors',doctor_viewset)
router.register(r'parchi',Appointment_viewset)
urlpatterns=[
    path('',include(router.urls))
]