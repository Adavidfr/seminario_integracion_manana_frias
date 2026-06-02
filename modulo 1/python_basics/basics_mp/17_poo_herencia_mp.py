# herencia.py - Jerarquía de empleados en la empresa

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self._salario = salario     # _ → convención "protegido"
        self._bonificacion = 0      # bonificación acumulada

    def aumentar_salario(self, incremento):
        self._salario += incremento
        return self

    def dar_bonificacion(self, cantidad):
        self._bonificacion += cantidad
        return self

    def __str__(self):
        return f"{self.nombre} ({self.puesto}) — ${self._salario} + ${self._bonificacion} bono"

class Manager(Empleado):
    def __init__(self, nombre, puesto, salario, equipo=None):
        super().__init__(nombre, puesto, salario)
        self.equipo = equipo or []

    def agregar_empleado(self, empleado_id):
        self.equipo.append(empleado_id)

    def __str__(self):
        return f"{super().__str__()} ({len(self.equipo)} empleados a cargo)"

class Especialista(Empleado):
    def __init__(self, nombre, especialidad, salario):
        super().__init__(nombre, f"{especialidad}", salario)
        self.especialidad = especialidad

    def realizar_consultoría(self):
        return f"Consultoría de {self.especialidad} completada"

    def __str__(self):
        return f"{super().__str__()} (Especialista: {self.especialidad})"

class DirectorGeneral(Manager):
    def __init__(self, nombre, salario, presupuesto=0):
        super().__init__(nombre, "Director General", salario)
        self.__presupuesto = presupuesto
        self.__gastos = 0

    def autorizar_gasto(self, cantidad):
        if self.__gastos + cantidad <= self.__presupuesto:
            self.__gastos += cantidad
            return True
        return False

    @property
    def presupuesto_disponible(self):
        return self.__presupuesto - self.__gastos

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Presupuesto disponible: ${self.presupuesto_disponible}")

# Crear instancias
employee1 = Empleado("Ana García", "Analista", 1200)
manager1 = Manager("Luis Pérez", "Manager de Desarrollo", 2000, ["E01", "E02"])
especialista1 = Especialista("María López", "Seguridad Informática", 1800)
director = DirectorGeneral("Roberto Díaz", 3500, presupuesto=50000)

print(employee1)
print(manager1)
employee1.aumentar_salario(300).dar_bonificacion(100)
print(employee1)
print(especialista1.realizar_consultoría())
print(especialista1)
print(director)
