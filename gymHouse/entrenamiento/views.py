from django.shortcuts import render,redirect
from django.views import generic
from .models import Ejercicio, Rutina
from .forms import FormRutina, FormEjercicio

class Ejercicios(generic.ListView):
    model = Ejercicio
    template_name = "alumnos_entrenar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ejercicio_1 = Ejercicio.objects.get(pk=1)
        context["brazos"] = Ejercicio.objects.filter(nombre_tipo = ["brazos"])
        context["espalda"] = Ejercicio.objects.filter(nombre_tipo = ["espalda"])
        context["abdominales"] = Ejercicio.objects.filter(nombre_tipo = ["abdominales"])
        context["piernas"] = Ejercicio.objects.filter(nombre_tipo = ["piernas"])
        context["elongacion"] = Ejercicio.objects.filter(nombre_tipo = ["elongacion"])
        context["gluteos"] = Ejercicio.objects.filter(nombre_tipo = ["gluteos"])
        # print(type(ejercicio_1.nombre_tipo))
        return context

class EjerciciosAdmin(generic.View):
    model = Ejercicio
    template_name = "admin_entrenar.html"

    
    def get(self, request, *args, **kwargs):
        context = {}
        context["brazos"] = Ejercicio.objects.filter(nombre_tipo = ["brazos"])
        context["espalda"] = Ejercicio.objects.filter(nombre_tipo = ["espalda"])
        context["abdominales"] = Ejercicio.objects.filter(nombre_tipo = ["abdominales"])
        context["piernas"] = Ejercicio.objects.filter(nombre_tipo = ["piernas"])
        context["elongacion"] = Ejercicio.objects.filter(nombre_tipo = ["elongacion"])
        context["gluteos"] = Ejercicio.objects.filter(nombre_tipo = ["gluteos"])
        return render(request,self.template_name,context)


    def post(self, request, *args, **kwargs):
        button_submit = request.POST

        if 'button_submit' in request.POST:
            print("Entro al rutinas")
            ejercicios = request.POST.getlist("ejercicios")
            ejercices = list(map(lambda x: Ejercicio.objects.get(pk=int(x)),ejercicios))
            
            fecha = request.POST.get("fecha")
            genero = request.POST.get("genero")
        
            new_rutine = Rutina(genero=genero,fecha=fecha)
            new_rutine.save()
            for ejercice in ejercices:
                # print(ejercice)
                new_rutine.ejercicios.add(ejercice)
    
            return redirect("entrenamiento:ejerciciosAdmin")

        elif 'button_submit_ejercicio' in request.POST:
            print("Entro al ejercicio")
            tipo = request.POST.get("nombre_tipo")
            nombre = request.POST.get("nombre")
            pasos = request.POST.get("pasos")
            archivo = request.POST.get("archivo")
            new_ejercicio = Ejercicio(nombre_tipo=tipo,nombre=nombre,pasos=pasos,archivo=archivo)
            new_ejercicio.save()
            return redirect("entrenamiento:ejerciciosAdmin")


class HistorialRutina(generic.View):
    model= Rutina
    template_name = "admin_entrenar-historial.html"

    def get(self,request,*args, **kwargs):
        context={}
        date = request.GET.get("fecha")
        rutina_hombre = Rutina.objects.filter(fecha=date,genero="hombre").last()
        rutina_mujer = Rutina.objects.filter(fecha=date,genero="mujer").last()
        print(rutina_mujer)

        try:
            try:
                ejercicios_woman = rutina_mujer.ejercicios.all()
            except:
                ejercicios_woman = []
            try:
                ejercicios_man = rutina_hombre.ejercicios.all()

            except:
                ejercicios_man =[]
            tipos_ejercicios_hombre = [ejercicio.nombre_tipo for ejercicio in ejercicios_man]
            tipos_ejercicios_woman = [ejercicio.nombre_tipo for ejercicio in ejercicios_woman]

            # for i in ejercicios_man:
            #     i.nombre_tipo

            list_types_man = []
            list_types_woman = []

            for i in tipos_ejercicios_hombre:
                list_types_man.append(i[0])
            for i in tipos_ejercicios_woman:
                list_types_woman.append(i[0])
            context["ejercicios_man"] =ejercicios_man
            context["ejercicios_woman"] = ejercicios_woman
            context["list_types_man"] = list_types_man
            context["list_types_woman"] = list_types_woman
        except:
            return render(request, self.template_name)

        

        return render(request, self.template_name,context)

    def post(self,request,*args, **kwargs):
        pass
        
    