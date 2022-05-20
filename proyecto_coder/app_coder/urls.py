from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path("curso",views.cursos),
    path("alta_curso/<nombre>", views.alta_curso)
]