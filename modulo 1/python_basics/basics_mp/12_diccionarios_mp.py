# diccionarios.py - Gestión de empleados

# Crear diccionarios
vacio    = {}
empleado  = {"nombre": "Ana García", "edad": 28, "ciudad": "Madrid"}
config   = dict(departamento="RR.HH", salario=1500, activo=True)

# Acceso
print(empleado["nombre"])              # Ana García
print(empleado.get("email"))           # None
print(empleado.get("email", "N/A"))    # N/A

# Modificar
empleado["email"]   = "ana@empresa.com"  # añadir/modificar
empleado["edad"]    = 29                  # modificar
del empleado["ciudad"]                    # eliminar
valor = empleado.pop("email")             # eliminar y obtener valor
print(empleado)

# Verificar existencia
print("nombre" in empleado)            # True
print("ciudad" in empleado)            # False

# Métodos esenciales
print(empleado.keys())    # dict_keys(['nombre', 'edad'])
print(empleado.values())  # dict_values(['Ana García', 29])
print(empleado.items())   # dict_items([('nombre', 'Ana García'), ('edad', 29)])

# Iterar
for clave, valor in empleado.items():
    print(f"  {clave}: {valor}")

# update — fusionar diccionarios
empleado.update({"ciudad": "Barcelona", "telefono": "600111222"})
print(empleado)

# Fusionar con | (Python 3.9+)
extra  = {"cargo": "Analista", "contratado": 2020}
completo = empleado | extra
print(completo)

# Diccionarios anidados
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        1: {"nombre": "Ana García", "depto": "Desarrollo"},
        2: {"nombre": "Luis Pérez", "depto": "Ventas"},
    },
    "sedes": ["Madrid", "Barcelona", "Valencia"]
}

print(empresa["empleados"][1]["nombre"])   # Ana García
empresa["empleados"][3] = {"nombre": "Marta López", "depto": "RR.HH"}

# setdefault — añadir solo si no existe
empleado.setdefault("pais", "España")       # añade "pais"
empleado.setdefault("nombre", "Otro")     # no modifica — ya existe
print(empleado)
