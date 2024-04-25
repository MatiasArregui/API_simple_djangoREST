# api_rest/api_alumnos/urls.py : api-alumnos urls.py
from django.urls import path
from api_alumnos.views import CarrerasList, CursoList, AlumnoList, CarreraDetail, CursoDetail, AlumnoDetail

urlpatterns = [
    path('CarrerasList/', CarrerasList.as_view()),
    path('CursosList/', CursoList.as_view()),
    path('AlumnosList/', AlumnoList.as_view()),
    path('CarreraDetail/<int:pk>/', CarreraDetail.as_view()),
    path('CursoDetail/<int:pk>/', CursoDetail.as_view()),
    path('AlumnoDetail/<int:pk>/', AlumnoDetail.as_view()),
    ]

