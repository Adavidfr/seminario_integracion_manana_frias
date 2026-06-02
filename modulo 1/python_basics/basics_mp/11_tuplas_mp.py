# tuplas.py - Datos de empleados

# Crear tuplas
vacia      = ()
unitaria   = (1001,)          # la coma es obligatoria para tupla de un elemento
registro_simple = ("E200", "Ana García")
evaluacion = (9.5, 8.7, 9.2)  # calificaciones trimestrales
empleado    = ("Luis Pérez", 30, "Desarrollo")

# Tupla sin paréntesis
punto  = 1001, "Técnico"      # también es una tupla
print(type(punto))            # <class 'tuple'>

# Acceso igual que las listas
print(empleado[0])           # Luis Pérez
print(empleado[-1])          # Desarrollo
print(empleado[1:])          # (30, 'Desarrollo')

# Las tuplas son INMUTABLES
# empleado[0] = "María"       # TypeError

# Desempaquetado (unpacking)
nombre, edad, depto = empleado
print(f"{nombre}, {edad} años, {depto}")  # Luis Pérez, 30 años, Desarrollo

# Desempaquetado con *
primero, *resto = (1001, 1002, 1003, 1004, 1005)
print(f"Primer ID: {primero}")    # 1001
print(f"Resto: {resto}")          # [1002, 1003, 1004, 1005]

*inicio, ultimo = (1001, 1002, 1003, 1004, 1005)
print(f"IDs iniciales: {inicio}")  # [1001, 1002, 1003, 1004]
print(f"Último: {ultimo}")          # 1005

# Tuplas de retorno de funciones
def evaluar_empleado(calificacion):
    if calificacion >= 8:
        return True, "Cumple expectativas"
    return False, "Necesita mejora"

resultado, mensaje = evaluar_empleado(8.5)
if resultado:
    print(f"✓ {mensaje}")
else:
    print(f"✗ {mensaje}")

# Tuplas como claves de diccionario (las listas NO pueden ser claves)
mapeo_departamento = {(1, "Dev"): "Desarrollo", (2, "RH"): "Recursos Humanos", (3, "Fin"): "Finanzas"}
print(mapeo_departamento[(1, "Dev")])   # Desarrollo
