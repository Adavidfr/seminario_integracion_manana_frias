# abstraccion.py - Tipos de empleados con contrato distinto
from abc import ABC, abstractmethod

# ABC (Abstract Base Class) — clase abstracta que no puede instanciarse
class ContratoEmpleado(ABC):
    def __init__(self, nombre, duración="Indefinido"):
        self.nombre = nombre
        self.duración = duración

    # Método abstracto — CADA subclase DEBE implementarlo
    @abstractmethod
    def calcular_beneficios(self) -> float:
        pass

    @abstractmethod
    def tipo_seguro(self) -> str:
        pass

    # Método concreto — compartido por todos los contratos
    def describir(self) -> str:
        return (f"{self.__class__.__name__} - {self.nombre}: "
                f"duración={self.duración}, beneficios=${self.calcular_beneficios():.2f}, "
                f"seguro={self.tipo_seguro()}")

# ContratoEmpleado()  # TypeError — no puede instanciarse

class ContratoPermanente(ContratoEmpleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Indefinido")

    def calcular_beneficios(self):
        return 500.0  # beneficios completos

    def tipo_seguro(self):
        return "Seguro médico premium"

class ContratoTemporal(ContratoEmpleado):
    def __init__(self, nombre, meses=6):
        super().__init__(nombre, f"{meses} meses")
        self.meses = meses

    def calcular_beneficios(self):
        return 200.0  # beneficios básicos

    def tipo_seguro(self):
        return "Seguro médico básico"

class ContratoContratista(ContratoEmpleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Por proyecto")

    def calcular_beneficios(self):
        return 0.0  # sin beneficios

    def tipo_seguro(self):
        return "Responsabilidad civil"

# Polimorfismo — mismo código para cualquier Contrato
contratos = [
    ContratoPermanente("Ana García"),
    ContratoTemporal("Luis Pérez", 12),
    ContratoContratista("María López")
]

for contrato in contratos:
    print(contrato.describir())

beneficio_total = sum(c.calcular_beneficios() for c in contratos)
print(f"Beneficio total: ${beneficio_total:.2f}")
