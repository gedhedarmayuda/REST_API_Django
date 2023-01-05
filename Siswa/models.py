from django.db import models

# Create your models here.


class Siswa(models.Model):
    no_siswa = models.CharField(max_length=5)
    nama = models.CharField(max_length=20)
    usia = models.IntegerField()
    nama_wali = models.CharField(max_length=20)
