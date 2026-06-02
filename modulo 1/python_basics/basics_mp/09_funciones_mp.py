print('Funciones en Recursos Humanos')
print('Funcion basica')

def bienvenida_rrhh():
    print('Bienvenido al sistema de RR.HH.')

bienvenida_rrhh()

print('Funcion con parametros')
def registrar_empleado(nombre):
    print(f'Empleado registrado: {nombre}')

registrar_empleado('Ana García')
registrar_empleado('Luis Pérez')

print('Funcion que devuelve valor con return')
def calcular_salario_neto(bruto, descuentos):
    return bruto - descuentos

print(calcular_salario_neto(2000, 300))

print('Funcion con valor por posicion')
def contratacion(nombre, puesto, salario):
    print(f'{nombre} - Puesto: {puesto} - Salario: {salario}')
contratacion('Marta Silva', 'Analista', 1200)  #por posicion
contratacion(salario=1500, nombre='Carlos', puesto='Manager') #por nombre

print('Funcion con valor por defecto')
def resumen_empleado(nombre, departamento="RR.HH", estado="Activo"):
    print(f'{nombre} - {departamento} - Estado: {estado}')
resumen_empleado('Diana López', "Finanzas", "Activo")
resumen_empleado("Juan", estado="Licencia")
resumen_empleado("Roberto")

print('Funcion parametros posicionales')
def calcular_promedio_salarios(*salarios):
    print(f"Salarios: {salarios}")
    return sum(salarios) / len(salarios) if salarios else 0

print(f"Promedio: {calcular_promedio_salarios(1200, 1500, 1100):.2f}")
print(f"Promedio: {calcular_promedio_salarios(2000, 2500, 3000, 1800):.2f}")

print('Devolver multiples valores')
def calcular_salario_stats(salarios):
    return min(salarios), max(salarios), sum(salarios)/len(salarios)

minimo, maximo, promedio = calcular_salario_stats([1200, 1500, 1100, 1800])
print(f"Mín: {minimo}, Máx: {maximo}, Promedio: {promedio:.2f}")

print('Devolver un diccionario con múltiples valores')
def analizar_nomina(salarios):
    total = sum(salarios)
    n = len(salarios)
    return {
        "total": total,
        "promedio": total/n if n > 0 else 0,
        "minimo": min(salarios) if salarios else None,
        "maximo": max(salarios) if salarios else None,
        "cantidad": n
    }
nominas = [1200, 1500, 1100, 1800]
stats = analizar_nomina(nominas)
print(f"Total nómina: {stats['total']}")
print(f"Promedio: {stats['promedio']:.2f}")
