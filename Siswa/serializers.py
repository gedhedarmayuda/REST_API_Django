from rest_framework import serializers
from Siswa.models import Siswa


class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        field = '__all__'
