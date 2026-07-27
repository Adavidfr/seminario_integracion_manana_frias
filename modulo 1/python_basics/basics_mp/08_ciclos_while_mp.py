contador = 1
while (contador <= 5):
    print(f"ID Empleado: {1000 + contador}")
    contador += 1

print("Control del ciclo")
print("continue")
i = 1
while (i <= 5):
    i += 1
    if i == 3:
        continue
    print(f"Procesando empleado {i}")

print("break")
i = 1
while (i <= 5):
    if i == 3:
        break
    print(f"Empleado: {i}")
    i += 1

id_empleado = int(input("Ingrese ID de empleado: "))
while id_empleado != 0:
    print("ID registrado:", id_empleado)
    id_empleado = int(input("Ingrese ID de empleado (0 para salir): "))

contador = 1
while (contador <= 5):
    print(f"Fila {contador} de datos")
    contador += 1
else:
    print("Proceso completado")

contador = 1
while True:
    print(f"Contador: {contador}")
    contador += 1
    if not (contador <= 5):
        break

contrasena_sistema = "admin123"
while True:
    entrada = input("Ingrese contraseña del sistema: ")
    if entrada == contrasena_sistema:
        print("Acceso permitido")
        break
    else:
        print("Contraseña incorrecta")
