from django.db import models

# Create your models here.

class Siswa(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=20, blank=False)
    usia = models.IntegerField()