print("Listas de empleados")
print("Crear Listas")
vacia = []
print(vacia)
ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
print(ids)
empleados = ["Ana García", "Luis Pérez", "Carmen López", "Roberto Díaz", "Sofía Ruiz", "Javier Torres"]
print(empleados)
mixta = [1001, "Ana", "RR.HH", True, None, 1500.5]
print(mixta)
anidada = [1, [1001, ["Ana", "Manager"]], 2, 3]
print(anidada)

print("Acceso a los elementos de una lista")
print(empleados[0])
print(empleados[-1])
print(empleados[1:3])
print(empleados[::-1])

print("CRUD de una lista")
# agregar
departamentos = ['RR.HH', 'Desarrollo', 'Finanzas', 'Ventas']
departamentos.append('Logística')
print(departamentos)
departamentos.insert(1, 'Marketing')
print(departamentos)
departamentos.extend(['Auditoría', 'Legal'])
# modificar
departamentos[0] = "Recursos Humanos"
print(departamentos)
# eliminar elementos
departamentos.remove('Ventas')
print(departamentos)
eliminado = departamentos.pop()
print(departamentos)
eliminado = departamentos.pop(0)
print(departamentos)
del departamentos[0]
print(departamentos)

print("Buscar valores en los elementos de una lista")
print('Legal' in departamentos)
print(departamentos.index('Logística'))
print(departamentos.count('Desarrollo'))

print("Ordenar una lista")
salarios_desordenados = [1500, 1200, 2000, 1000, 1800, 1100]
print(salarios_desordenados)
salarios_desordenados.sort()
print(salarios_desordenados)
