from django.db import models

from django.db import models

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Ej: perro, gato
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
class CitaMedica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.mascota} con {self.veterinario} en {self.fecha}"
class Tratamiento(models.Model):
    cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    duracion = models.IntegerField()  # en días

    def __str__(self):
        return f"Tratamiento para {self.cita.mascota} ({self.medicamento})"
class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"Historial de {self.mascota} ({self.cita.fecha})"
class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_administracion = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vacuna {self.nombre} para {self.mascota}"
class Factura(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Factura para {self.mascota} ({self.fecha})"
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
class ServicioEnCita(models.Model):
    cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servicio} en la cita de {self.cita.mascota}"
