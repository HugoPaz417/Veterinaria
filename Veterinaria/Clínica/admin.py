from django.contrib import admin
from .models import (
    Mascota, Veterinario, CitaMedica, HistorialMedico, 
    Tratamiento, Servicio, Vacuna, Dueño, Factura, 
    ServicioEnCita
)

# Registra los modelos para que aparezcan en el admin
admin.site.register(Mascota)
admin.site.register(Veterinario)
admin.site.register(CitaMedica)
admin.site.register(HistorialMedico)
admin.site.register(Tratamiento)
admin.site.register(Servicio)
admin.site.register(Vacuna)
admin.site.register(Dueño)
admin.site.register(Factura)
admin.site.register(ServicioEnCita)
