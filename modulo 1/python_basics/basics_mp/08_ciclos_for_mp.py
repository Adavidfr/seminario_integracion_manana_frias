print("ciclo for")
empleados = ["Ana García", "Luis Pérez", "Carmen López", "Roberto Díaz", "Sofía Ruiz"]
for empleado in empleados:
    print(empleado)

print("Recorrer caracteres en departamento")
for letra in "RRHH":
    print(letra)

print("Recorrer rango de IDs")
for id_num in range(1001, 1006):
    print(f"ID Empleado: {id_num}")

print("Recorrer rango configurar paso")
for semana in range(1, 13, 2):
    print(f"Semana {semana}")

print("Enumerar Lista de empleados")
for i, empleado in enumerate(empleados):
    print(f"Posición {i}: {empleado}")

print("Dos listas a la vez")
nombres = ["Ana", "Luis", "Carmen"]
salarios = [1200, 1500, 1100]
for nombre, salario in zip(nombres, salarios):
    print(f"{nombre}: {salario} USD")

print("control del ciclo - break")
for i in range(10):
    if i == 3:
        break
    print(i)

print("continue")
for i in range(10):
    if i == 2:
        continue
    print(i)

print("for anidado")
for depto in range(2):
    for empleado in range(3):
        print(f"Depto {depto}, Empleado {empleado}")

print("List comprehension - calcular bonos")
bonos = [salario * 0.1 for salario in [1000, 1500, 2000]]
print(bonos)
