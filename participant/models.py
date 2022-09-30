from django.db import models


class Participant(models.Model):
    reference_number = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reference_number}"
