from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import CustomUser


class Patient(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    biography = models.CharField(max_length=512)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    details = models.TextField(max_length=512)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'P: {}, D: {}'.format(self.patient, self.doctor)