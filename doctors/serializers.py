from rest_framework import serializers
from doctors.models import doctor , Appointment
class doctorserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=doctor
        fields='__all__'

    
class Appointmentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'