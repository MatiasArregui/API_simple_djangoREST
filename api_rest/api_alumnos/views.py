from django.shortcuts import render

# Create your views here.
# api_alumnos/views.py


from django.http import Http404
from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from api_alumnos.models import Carreras, Cursos, Alumnos
from api_alumnos.serializers import CarrerasSerializer, CursoSerializer, AlumnoSerializer


class CarrerasList(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, format=None):
        '''
        Obtiene todas las carreras existentes.
        '''
        carreras = Carreras.objects.all()
        serializer = CarrerasSerializer(carreras, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        '''
        Crea una carrera con los datos enviados.
        '''
        serializer = CarrerasSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CursoList(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, format=None):
        '''
        Obtiene todos los cursos existentes.
        '''
        cursos = Cursos.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        '''
        Crea un curso con los datos enviados.
        '''
        serializer = CursoSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlumnoList(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, format=None):
        '''
        Obtiene todos los alumnos existentes.
        '''
        alumnos = Alumnos.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        '''
        Crea un alumno con los datos enviados.
        '''
        serializer = AlumnoSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarreraDetail(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self, pk):
        try:
            return Carreras.objects.get(pk=pk)
        except Carreras.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        '''
        Obtiene una carrera por su id.
        '''
        carrera = self.get_object(pk)
        serializer = CarrerasSerializer(carrera)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        '''
        Actualiza una carrera por su id.
        '''
        carrera = self.get_object(pk)
        serializer = CarrerasSerializer(carrera, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        '''
        Elimina una carrera por su id.
        '''
        carrera = self.get_object(pk)
        carrera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CursoDetail(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self, pk):
        try:
            return Cursos.objects.get(pk=pk)
        except Cursos.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        '''
        Obtiene un curso por su id.
        '''
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        '''
        Actualiza un curso por su id.
        '''
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        '''
        Elimina un curso por su id.
        '''
        curso = self.get_object(pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlumnoDetail(APIView):
    # agregar permiso para verificar si el usuario está autenticado.
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self, pk):
        try:
            return Alumnos.objects.get(pk=pk)
        except Alumnos.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        '''
        Obtiene un alumno por su id.
        '''
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        '''
        Actualiza un alumno por su id.
        '''
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        '''
        Elimina a un alumno por su id.
        '''
        alumno = self.get_object(pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)