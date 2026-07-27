" ENTEROS, CADENA DE CARACTERES, BOOLEANOS, NONE"
nombre="David García" # string
id_empleado= 1005 # int
salario= 1850.50 # float
activo=True # boolean
empleado_provisional= None # NoneType

print(type(nombre))
print(type(id_empleado))
print(type(salario))
print(type(activo))
print(type(empleado_provisional))

#Asignar valor varias variables en una linea
e1, e2, e3= 101, 102, 103
print(e1)
print(e2)
print(e3)

# Asignar el mismo valor a varias variables
e1= e2 = e3 = 105
print(e1)
print(e2)
print(e3)

#Intercambiar valores
id1,id2= 1000, 2000
print(id1,id2)
id1,id2= id2,id1
print(id1,id2)

#Convenciones de nombres
nombre_completo= "David García" # snake_case
nombreCompleto= "David García" # NO USAR camelCase
MAX_EMPLEADOS=50 # MAYUSCULAS SOSTENIDAS PARA CONSTANTES
_departamento_interno= "privado" # para uso interno

#Manejo de Enteros
id_pequeno = 42
id_negativo = -77
id_grande = 1_000_000
id_enorme= 2 ** 20

print(id_pequeno)
print(id_negativo)
print(id_grande)
print(id_enorme)
