from django.db import models

# Create your models here.

class doctor(models.Model):
    sr_no=models.PositiveIntegerField()

    name=models.CharField( max_length=50)
    
    location=models.CharField( max_length=50)
    type=models.CharField( max_length=50,choices=(('suregon','suregon'),('nuerologist','nuerologist')))
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name +'--' + self.type


class Appointment(models.Model):
    Sr_no=models.PositiveIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    client_name = models.CharField(max_length=100)
    
