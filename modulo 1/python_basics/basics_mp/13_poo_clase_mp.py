# clase.py - Modelo de Empleado

class Empleado:
    # Atributo de clase — compartido por TODAS las instancias
    organización = "TechCorp"

    # __init__ es el constructor — se ejecuta al crear la instancia
    def __init__(self, id_empleado, nombre, puesto):
        # Atributos de instancia — propios de cada objeto
        self.id = id_empleado
        self.nombre = nombre
        self.puesto = puesto

    # Método de instancia — self es la referencia al objeto
    def presentarse(self):
        return f"Soy {self.nombre}, {self.puesto}."

    def ascender(self, nuevo_puesto):
        puesto_anterior = self.puesto
        self.puesto = nuevo_puesto
        print(f"✓ {self.nombre} ascendido de {puesto_anterior} a {nuevo_puesto}")

    # __str__ — representación legible (para print y str())
    def __str__(self):
        return f"Empleado({self.nombre}, {self.puesto})"

    # __repr__ — representación oficial (para depuración)
    def __repr__(self):
        return f"Empleado(id={self.id!r}, nombre={self.nombre!r}, puesto={self.puesto!r})"

# Crear instancias (objetos) con la clase como función
ana = Empleado(1001, "Ana García", "Analista")
luis = Empleado(1002, "Luis Pérez", "Desarrollador")

print(ana.presentarse())       # Soy Ana García, Analista.
print(luis.presentarse())      # Soy Luis Pérez, Desarrollador.
ana.ascender("Senior Analista")        # ✓ Ana García ascendido de Analista a Senior Analista
print(str(ana))            # Empleado(Ana García, Senior Analista)
print(repr(ana))           # Empleado(id=1001, nombre='Ana García', puesto='Senior Analista')
print(Empleado.organización)     # TechCorp  — atributo de clase
