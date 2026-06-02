# encapsulamiento.py - Legajo de empleado con información privada

class LegajoEmpleado:
    def __init__(self, nombre, salario_inicial=0):
        self.nombre      = nombre
        self.__salario    = salario_inicial     # __ — privado (name mangling)
        self.__historial_salarios = []
        self.__activo   = True
        self.__registrar(f"Legajo creado con salario inicial ${salario_inicial}")

    # Property — getter (acceso como atributo, no como método)
    @property
    def salario_actual(self):
        return self.__salario

    @property
    def activo(self):
        return self.__activo

    @property
    def historial_salarios(self):
        return list(self.__historial_salarios)   # devuelve copia, no referencia

    # Método público — la "ventanilla"
    def aumentar_salario(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        salario_anterior = self.__salario
        self.__salario += cantidad
        self.__registrar(f"Aumento de salario: +${cantidad} (${salario_anterior} → ${self.__salario})")
        return self

    def reducir_salario(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__salario:
            raise ValueError(f"Reducción mayor al salario actual (${self.__salario})")
        self.__salario -= cantidad
        self.__registrar(f"Reducción de salario: -${cantidad}")
        return self

    def transferencia_bonificación(self, monto, otro_legajo):
        self.reducir_salario(monto)
        otro_legajo.aumentar_salario(monto)
        self.__registrar(f"Bonificación transferida a {otro_legajo.nombre}: -${monto}")
        return self

    # Método privado — solo para uso interno
    def __registrar(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__historial_salarios.append(f"[{hora}] {operacion}")

    def dar_baja(self):
        self.__activo = False
        self.__registrar("Empleado dado de baja")

    def __str__(self):
        return f"Legajo({self.nombre}: ${self.__salario})"

# Uso
l1 = LegajoEmpleado("Ana García", 1000)
l2 = LegajoEmpleado("Luis Pérez", 500)

l1.aumentar_salario(500).reducir_salario(200)     # encadenamiento
l1.transferencia_bonificación(300, l2)

print(l1)    # Legajo(Ana García: $1000)
print(l2)    # Legajo(Luis Pérez: $800)
print(f"Salario Ana: ${l1.salario_actual}")   # acceso como atributo (property)

# l1.__salario = 99999  # AttributeError — acceso directo denegado
# l1.salario_actual = 99999    # AttributeError — no hay setter

for entrada in l1.historial_salarios:
    print(f"  {entrada}")
