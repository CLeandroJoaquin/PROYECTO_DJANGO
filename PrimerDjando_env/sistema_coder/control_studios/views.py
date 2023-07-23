from django.shortcuts import render

# Create your views here.

def listar_estudiantes(request):
    contexto={
        "estudiantes":[
            {"nombre":"Emanuel", "apellido":"Ortega", "nota":10},
            {"nombre":"Manuela", "apellido":"Diaz", "nota":3},
            {"nombre": "Gonzalo", "apellido":"Castillo", "nota":7},
            {"nombre": "Carlos", "apellido":"Perez", "nota":8},
        ]
    }
    http_response= render(
        request= request,
        template_name="control_studios/lista_estudiantes.html",
        context=contexto,
        )
    return http_response


def listar_cursos(request):
    contexto={
        "cursos":[
            {"nombre":"Fisica", "comision":1000},
            {"nombre":"Python", "comision":55350},
            {"nombre": "Redes Sociales", "comision":2000},
            
        ]
    }
    http_response= render(
        request= request,
        template_name="control_studios/lista_cursos.html",
        context=contexto,
        )
    return http_response