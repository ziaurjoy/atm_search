from django.db import models

# Create your models here.

class BusCompany(models.Model):
    name = models.CharField(max_length=100)
    head_office = models.TextField()
    starft_count = models.IntegerField()
    def __str__(self):
        return self.name
