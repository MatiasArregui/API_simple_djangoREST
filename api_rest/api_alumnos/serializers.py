# api_alumnos/serializers.py
from rest_framework import serializers
from api_alumnos.models import Carreras, Cursos, Alumnos


class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'