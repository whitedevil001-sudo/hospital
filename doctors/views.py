from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from doctors.models import doctor, Appointment
from doctors.serializers import doctorserializer,Appointmentserializer
class doctor_viewset(viewsets.ModelViewSet):
    queryset=doctor.objects.all()
    serializer_class=doctorserializer


class Appointment_viewset(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=Appointmentserializer
